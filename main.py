from fastapi import FastAPI
import json
import os

app = FastAPI()

MEM_FILE = "memoria.json"

def load_memory():
    if os.path.exists(MEM_FILE):
        with open(MEM_FILE, "r") as f:
            return json.load(f)
    return {"chat": []}

def save_memory(data):
    with open(MEM_FILE, "w") as f:
        json.dump(data, f)

memoria = load_memory()


def jarvis(text: str):
    text = text.lower()

    # guardar mensaje en historial
    memoria["chat"].append({"user": text})

    # lógica básica de contexto
    if "hola" in text:
        response = "Sistema activo."

    elif "como me llamo" in text:
        response = "Aún no tengo tu nombre guardado."

    elif "historial" in text:
        response = str(memoria["chat"][-5:])  # últimos 5 mensajes

    else:
        response = "Mensaje procesado."

    memoria["chat"].append({"jarvis": response})
    save_memory(memoria)

    return response


@app.get("/")
def home():
    return {"status": "Jarvis online"}

@app.get("/ask")
def ask(text: str):
    return {"response": jarvis(text)}
