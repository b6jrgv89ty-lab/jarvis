from fastapi import FastAPI
import json
import os

app = FastAPI()

MEM_FILE = "memoria.json"

def load_memory():
    if os.path.exists(MEM_FILE):
        with open(MEM_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(data):
    with open(MEM_FILE, "w") as f:
        json.dump(data, f)

memoria = load_memory()


def jarvis(text: str):
    text = text.lower()

    # guardar nombre
    if "mi nombre es " in text:
        nombre = text.replace("mi nombre es ", "")
        memoria["nombre"] = nombre
        save_memory(memoria)
        return f"Entendido, {nombre}."

    # recuperar nombre
    if "como me llamo" in text:
        return f"Te llamas {memoria.get('nombre', 'no lo sé aún')}."

    # saludo
    if "hola" in text:
        return "Sistema activo."

    return "No entendido."


@app.get("/")
def home():
    return {"status": "Jarvis online"}

@app.get("/ask")
def ask(text: str):
    return {"response": jarvis(text)}
