# SkillScope-AI

**SkillScope-AI** is a local-first modular AI agent capable of understanding voice, image, and PDF input through LangChain, Ollama, Whisper, and FastAPI. This project is designed to showcase clean backend architecture, multi-modal input handling, and agent memory.

## 🚀 Features
- 🧠 LLM integration (Ollama + LangChain)
- 🗣️ Voice input via OpenAI Whisper
- 📄 PDF parsing (PyMuPDF)
- 🖼️ OCR from images (Tesseract)
- 💬 Session-based memory (LangChain Memory / ChromaDB-ready)
- 🐳 Dockerized for portability
- 🔌 RESTful API using FastAPI

## 🛠️ Tech Stack
- Python, FastAPI
- Ollama, LangChain
- Whisper, pytesseract, PyMuPDF
- Docker, uvicorn

## 📦 Installation
```bash
git clone https://github.com/yourusername/skillscope-ai.git
cd skillscope-ai
docker-compose up --build
```

## 📬 API Endpoints
- `POST /chat` — LLM interaction
- `POST /voice` — Transcribe + respond to voice
- `POST /file/pdf` — Upload and analyze PDF
- `POST /file/image` — OCR and respond

## 🎥 Demo
(Include .gif or video demo here)

## 📄 License
MIT
