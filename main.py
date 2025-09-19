import argparse
import os
from dotenv import load_dotenv
import PyPDF2

from graph.workflow import build_graph

# Load environment variables from .env file
load_dotenv()

def main():
    """
    Main function to run the CV analysis multi-agent system.
    
    It parses command-line arguments for the CV file path and the target role,
    initializes the LangGraph application, and executes the workflow.
    The final report is printed to the console and saved to a file.
    """
    # --- Argument Parsing ---
    parser = argparse.ArgumentParser(description="AI-Augmented CV Analysis System")
    parser.add_argument(
        "--cv-path",
        type=str,
        required=True,
        help="Path to the candidate's CV file (.txt or .pdf format)."
    )
    parser.add_argument(
        "--role",
        type=str,
        required=True,
        help="The target job role for the analysis (e.g., 'Senior AI Engineer')."
    )
    args = parser.parse_args()

    # --- API Key Validation ---
    if not os.getenv("GOOGLE_API_KEY") or not os.getenv("TAVILY_API_KEY"):
        raise ValueError(
            "API keys for Google and Tavily are required. "
            "Please set GOOGLE_API_KEY and TAVILY_API_KEY in a .env file."
        )

    # --- File Reading ---
    cv_text = ""
    file_path = args.cv_path
    try:
        if file_path.lower().endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as f:
                cv_text = f.read()
        elif file_path.lower().endswith('.pdf'):
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        cv_text += page_text
        else:
            print(f"Error: Unsupported file format. Please provide a .txt or .pdf file.")
            return

        if not cv_text.strip():
            print(f"Warning: Could not extract text from the file: {file_path}")
            return

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading or processing the file: {e}")
        return

    # --- Graph Initialization ---
    app = build_graph()

    # --- Workflow Execution ---
    initial_state = {
        "cv_text": cv_text,
        "target_role": args.role,
    }

    print(f"Starting analysis for role: {args.role}...")
    final_state = app.invoke(initial_state)

    # --- Output ---
    final_report = final_state.get("final_report")
    if final_report:
        print("\n--- FINAL REPORT ---")
        print(final_report)

        # Save the report to a file
        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)
        report_path = os.path.join(output_dir, "final_report.md")
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(final_report)
        print(f"\nReport saved to {report_path}")
    else:
        print("Error: Could not generate the final report.")
        print("Final state:", final_state)


if __name__ == "__main__":
    main()

