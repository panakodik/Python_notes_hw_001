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
    
def save_notes(notes):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)

def create_note(title, body):
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка создана успешно!")