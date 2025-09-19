
---

# 🤖 AI Multi-Agent CV Analysis System

An intelligent AI system that serves as a **technical recruiter's assistant**, performing deep analysis on candidate CVs to uncover their true potential.

---

## 🎯 Project Objective

This project aims to build an AI system that goes beyond simple keyword matching. It:

* Comprehensively analyzes a candidate's CV for specialized technical roles (e.g., **Senior AI Engineer**).
* Identifies both explicit and implicit skills.
* Compares them against current market demands.
* Generates a **personalized skill-gap analysis** and **concrete upskilling path**.

The goal is to augment the recruiter's capabilities with deep, data-driven insights.

---

## 🏗️ Architecture Overview

The system is orchestrated using the **LangGraph framework** and powered by the **Google Gemini language model**.
Its workflow is structured as a **state machine** with four specialized agents working collaboratively:

1. **🕵️‍♂️ CV Parsing & Normalization Agent (The Data Engineer)**

   * Ingests raw CVs (.txt or .pdf).
   * Transforms them into structured, machine-readable JSON format.

2. **🧑‍💻 Specialized Skill Analyst Agent (The Subject Matter Expert)**

   * Analyzes structured CV data.
   * Infers **implicit skills** (e.g., Flask usage → REST APIs).
   * Identifies transferable skills.

3. **📈 Market Intelligence Agent (The Market Researcher)**

   * Uses the **Tavily API** to summarize industry trends.
   * Extracts in-demand skills from recent job postings for the target role.

4. **✍️ Recommendation & Report Agent (The Strategist & Communicator)**

   * Synthesizes all analyses.
   * Produces a final, comprehensive **Markdown report**.

---

## 📂 Project Structure

```plaintext
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
```

---

## 🛠️ Setup and Installation

Follow these steps to set up and run the project locally.

### Step 1: Clone the Repository

```bash
git clone https://github.com/rivaldofauzan/cv-agent-system.git
cd cv-agent-system
```

### Step 2: Create a Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies.

#### Windows

```bash
python -m venv agent
.\agent\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv agent
source agent/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up API Keys

This project requires API keys for **Google (Gemini)** and **Tavily**.

1. Create a new file named `.env` in the root directory.
2. Add your API keys in the following format:

```env
GOOGLE_API_KEY="AI..."
TAVILY_API_KEY="tvly-..."
```

Replace the values with your actual API keys.

---

## 🚀 How to Run the Application

Once dependencies and API keys are set up, run the analysis:

### Command Format

```bash
python main.py --cv-path "path/to/your/cv.pdf" --role "Target Role Name"
```

### Usage Example

```bash
python main.py --cv-path "CV_Rivaldo_Fauzan_Robani.pdf" --role "Senior AI Engineer"
```

The final report will be automatically saved in the **output/** directory.

---

Do you want me to also make this into a **professional GitHub README.md** (with badges, quickstart, and contribution sections), or keep it as a simple internal documentation file?
