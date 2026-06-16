# 🛠️ App Builder

**App Builder** is an AI-powered application generation assistant built with [LangGraph](https://github.com/langchain-ai/langgraph).  
It works like a multi-agent development team that can take a natural language request and transform it into a complete, working project — file by file — using real developer workflows.

---

## 🏗️ Architecture

- **Planner Agent** – Analyzes your request and generates a detailed project plan.
- **Architect Agent** – Breaks down the plan into specific engineering tasks with explicit context for each file.
- **Coder Agent** – Implements each task, writes directly into files, and uses available tools like a real developer.

The agent system is powered by:
- `graph.py` — graph utilities and flow orchestration.
- `nodes.py` — node definitions used inside graphs.
- `prompts.py` — prompt templates and helper functions.
- `states.py` — state management helpers.
- `tools.py` — small utility tools used by agents.

---

## 🚀 Getting Started

### Prerequisites

- Make sure you have Python 3.8+ installed.
- Ensure that you have created a Groq account and have your API key ready. Create an API key [here](https://console.groq.com/keys).

### ⚙️ Installation and Startup

- Create a virtual environment using: `python -m venv .venv` and activate it using `source .venv/bin/activate` (or `.venv\Scripts\activate` on Windows)
- Install the dependencies using: `pip install -r pyproject.toml`
- Create a `.env` file and add your Groq API key:
  ```
  GROQ_API_KEY=your_api_key_here
  ```

Now that we are done with all the set-up & installation steps we can start the application using the following command:

```bash
python main.py
```

### 🧪 Example Prompts

- Create a to-do list application using HTML, CSS, and JavaScript.
- Create a simple calculator web application.
- Create a simple blog API in FastAPI with a SQLite database.
- Build a weather dashboard with real-time data updates.
- Create a personal finance tracker with expense categories.

---

## 📁 Project Structure

```
App-Builder/
├── main.py                 # Entry point for the application
├── pyproject.toml         # Project dependencies and configuration
├── agent/                 # Agent implementation package
│   ├── graph.py          # Graph orchestration logic
│   ├── nodes.py          # Agent node definitions
│   ├── prompts.py        # Prompt templates
│   ├── states.py         # State management
│   └── tools.py          # Utility tools

```

---

## 💡 Usage

Run `python main.py` and follow the prompts to describe what you want to build. The agent system will:

1. **Plan** – Create a comprehensive project blueprint
2. **Design** – Break it into implementable tasks
3. **Code** – Generate all necessary files automatically
4. **Deploy** – Output a ready-to-run project

To view generated web demos, open the `generated_project/index.html` file in your browser.

---

## 🔧 Development

- Add or modify node implementations in `agent/nodes.py` and wire them into flows via `agent/graph.py`.
- Use `agent/tools.py` for shared helpers; keep `prompts.py` focused on text templates.
- Extend `states.py` to support additional state management needs.

---

## 📝 License

Copyright © 2026. All rights reserved.
