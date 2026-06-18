from fastapi import FastAPI

app = FastAPI()

def jarvis(text):
    text = text.lower()

    if "hola" in text:
        return "Sistema activo."

    if "hora" in text:
        from datetime import datetime
        return f"Hora actual: {datetime.now().strftime('%H:%M')}."

    return "No entendí el comando."


@app.get("/")
def home():
    return {"status": "Jarvis online"}

@app.get("/ask")
def ask(text: str):
    return {"response": jarvis(text)}
