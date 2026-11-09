# Google ADK Agents

My journey of learning and building AI agents using **Google Agent Development Kit (ADK)**.

## 📌 About

This repository contains my experiments, practice projects, and implementations while learning AI agent development with Google ADK.

## 🛠️ Tech Stack

- Python
- Google Agent Development Kit (ADK)
- LiteLLM
- OpenRouter

## 📂 Project Structure

```text
google_adk_agents/
├── batX_bot/
│   ├── __init__.py
│   ├── agent.py
│   └── .gitignore
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ankitrajofficial2005/google_adk.git
cd google_adk
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install google-adk litellm
```

### 4. Configure environment variables

Create a `.env` file and add your OpenRouter API key:

```env
OPENROUTER_API_KEY=your_api_key_here
```

**Important:** Never commit your `.env` file or expose your API key.

### 5. Run the agent

```bash
adk web
```

## 🎯 Learning Goals

- Understand AI agents and agent architecture.
- Build agents using Google ADK.
- Experiment with different LLM providers.
- Explore tools, multi-agent systems, and agent workflows.

## 📈 Progress

This repository is a work in progress. More experiments and projects will be added as I learn.

---

⭐ Learning by building, one agent at a time.