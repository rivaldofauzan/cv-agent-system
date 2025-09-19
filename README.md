🤖 AI Multi-Agent CV Analysis System
An intelligent AI system that serves as a technical recruiter's assistant, performing deep analysis on candidate CVs to uncover their true potential.

🎯 Project Objective
This project aims to build an AI system that goes beyond simple keyword matching. It comprehensively analyzes a candidate's CV for specialized technical roles (e.g., Senior AI Engineer). By identifying both explicit and implicit skills, comparing them against current market demands, the system generates a personalized skill-gap analysis and a concrete upskilling path. The goal is to augment the recruiter's capabilities with deep, data-driven insights.

🏗️ Architecture Overview
The system is orchestrated using the LangGraph framework and powered by the Google Gemini language model. Its workflow is structured as a state machine that facilitates collaboration between four specialized agents:

🕵️‍♂️ CV Parsing & Normalization Agent (The Data Engineer): Ingests a raw CV (.txt or .pdf) and transforms it into a structured, machine-readable JSON format.

🧑‍💻 Specialized Skill Analyst Agent (The Subject Matter Expert): Analyzes the structured CV data to infer implicit skills (e.g., a project using Flask implies knowledge of REST APIs) and transferable skills.

📈 Market Intelligence Agent (The Market Researcher): Uses a search tool (Tavily API) to summarize industry trends and the most in-demand skills from recent job postings for the target role.

✍️ Recommendation & Report Agent (The Strategist & Communicator): Synthesizes all analyses to generate a final, comprehensive report in Markdown format.

📂 Project Structure
cv-agent-system/
├── agents/
│   ├── cv_parser.py
│   ├── skill_analyst.py
│   ├── market_intel.py
│   └── report_generator.py
├── graph/
│   ├── state.py
│   └── workflow.py
├── tools/
│   └── search.py
├── output/
│   └── report_YYYYMMDD_HHMMSS.md
├── .env
├── main.py
├── requirements.txt
├── sample_cv.txt
└── README.md

🛠️ Setup and Installation
Follow these steps to set up and run the project locally.

Step 1: Clone the Repository
git clone [<YOUR_REPOSITORY_URL>](https://github.com/rivaldofauzan/cv-agent-system.git)
cd cv-agent-system

Step 2: Create a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies.

# Windows
python -m venv agent
.\agent\Scripts\activate

# macOS / Linux
python3 -m venv agent
source agent/bin/activate

Step 3: Install Dependencies
Install all required libraries from the requirements.txt file.

pip install -r requirements.txt

Step 4: Set Up API Keys
This program requires API keys for Google (Gemini) and Tavily.

Create a new file in the project's root directory named .env.

Open the .env file and add your API keys in the following format:

GOOGLE_API_KEY="AI..."
TAVILY_API_KEY="tvly-..."

Replace the values inside the quotes with your actual API keys.

🚀 How to Run the Application
Once all dependencies are installed and the API keys are configured, you can run the analysis from your terminal.

Command Format
python main.py --cv-path "path/to/your/cv.pdf" --role "Target Role Name"

Usage Examples
# Analyze a PDF CV for a Senior AI Engineer role
python main.py --cv-path "CV_Rivaldo_Fauzan_Robani.pdf" --role "Senior AI Engineer"

The final report will be automatically saved in the output directory.