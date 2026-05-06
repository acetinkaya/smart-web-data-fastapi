import json
import os

DATA_FILE = "data/currency_history.json"

def load_history():
    if not os.path.exists(DATA_FILE):
        return {
            "message": "Henüz kayıtlı kur verisi yok."
        }

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
