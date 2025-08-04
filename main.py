from fastapi import FastAPI, UploadFile, File
from agent.core import generate_response

app = FastAPI()
@app.post("/chat")
def chat(query: str):
    return {"response": generate_response(query)}
