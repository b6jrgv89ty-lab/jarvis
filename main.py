from fastapi import FastAPI
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def home():
    return {"status": "Jarvis AI online"}

@app.get("/ask")
def ask(text: str):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente tipo Jarvis, preciso y técnico."},
            {"role": "user", "content": text}
        ]
    )

    return {"response": response.choices[0].message.content}
