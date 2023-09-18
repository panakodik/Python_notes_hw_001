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

def list_notes():
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Создано: {note['created_at']}")

def read_note(note_id):
    for note in notes:
        if note["id"] == note_id:
            print(f"Заголовок: {note['title']}\nСоздано: {note['created_at']}\nТело: {note['body']}")
            return
    print("Заметка с указанным ID не найдена.")

def edit_note(note_id, new_title, new_body):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = new_title
            note["body"] = new_body
            note["updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка отредактирована успешно!")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note(note_id):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена успешно!")
            return
    print("Заметка с указанным ID не найдена.")

if __name__ == "__main__":
    notes = load_notes()

    while True:
        print("\nВыберите действие:")
        print("1. Создать заметку")
        print("2. Список заметок")
        print("3. Читать заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            create_note(title, body)
        elif choice == "2":
            list_notes()
        elif choice == "3":
            note_id = int(input("Введите ID заметки: "))
            read_note(note_id)
        elif choice == "4":
            note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
            new_title = input("Введите новый заголовок: ")
            new_body = input("Введите новый текст: ")
            edit_note(note_id, new_title, new_body)
        elif choice == "5":
            note_id = int(input("Введите ID заметки, которую хотите удалить: "))
            delete_note(note_id)
        elif choice == "6":
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")