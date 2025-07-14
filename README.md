# SkillScope-AI

**SkillScope-AI** is a local-first modular AI agent capable of understanding a multitude of inputs in order to process information. This project is designed to showcase clean backend architecture, multi-modal input handling, summarization, and agent memory.

Current Capabilities: Can understand and respond to voice, PDF, and image inputs using Whisper, PyMuPDF, Tesseract, and GPT-based LLMs. It supports intelligent interaction through LangChain and Ollama, with memory retention and a RESTful FastAPI backend. It can transcribe audio, summarize PDFs, extract text from images, and answer questions about all of them.

## 🚀 Features
- 🧠 LLM integration (Ollama + LangChain)
- 🗣️ Voice input via OpenAI Whisper
- 📄 PDF parsing and summarization (PyMuPDF + OpenAI)
- 🖼️ OCR from images (Tesseract)
- 💬 Session-based memory (LangChain Memory / ChromaDB-ready)
- 🐳 Dockerized for portability
- 🔌 RESTful API using FastAPI

## 🛠️ Tech Stack
- Python, FastAPI
- Ollama, LangChain, OpenAI
- Whisper, PyMuPDF, pytesseract
- Docker, uvicorn

## 📦 Installation
```bash
git clone https://github.com/sehajpandal01/skillscope-ai.git
cd skillscope-ai
docker-compose up --build
