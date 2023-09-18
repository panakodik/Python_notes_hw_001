import json
import os
import datetime

# Путь к файлу для хранения заметок
FILE_PATH = "notes.json"

def load_notes():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    else:
        return []