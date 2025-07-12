# SkillScope-AI

**SkillScope-AI** is a local-first modular AI agent capable of understanding voice, image, and PDF input through LangChain, Ollama, Whisper, and FastAPI. This project is designed to showcase clean backend architecture, multi-modal input handling, summarization, and agent memory.

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
