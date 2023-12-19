from note import Note
import json
import datetime

class Application:
    def __init__(self, file_name):
        self.file_name = file_name
        self.notes_file = self.open_notes_file(self.file_name)
        self.notes = ""

        if self.notes_file == "":
            self.last_note_id = 0
        else:
            self.notes = json.loads(self.notes_file)
            self.last_note_id = len(self.notes)

    def open_notes_file(self, file_name):
        try:
            stream = open(file_name, "r")
        except:
            stream = open(file_name, "x")
            stream.close()
            stream = open(file_name, "r")

        notes = stream.read()
        stream.close()

        return notes

    def command(self, command):
        match command:
            case "/add":
                self.add_note()
            case "/del":
                self.delete_note(input("Введите id удаляемой заметки: "))
            case "/edit":
                self.edit_note(input("Введите id редактируемой заметки: "))
            case "/show":
                self.show_note(input("Введите id заметки: "))
            case "/show_all":
                self.show_all_notes()
            case "/help":
                self.print_man_page()
            case _:
                self.print_man_page()

    def print_man_page(self):
        print("MAN PAGE:\n/add - Добавляет новую заметку\n/del - Удаляет заметку\n/edit - Редактирует заметку\n/show - Показывает заметку\n/show_all - Показывает все заметки\n/q - Выход из приложения")

    def add_note(self):
        self.note = Note(self.last_note_id + 1)

        self.note.set_head(input("Введите заголовок: "))
        self.note.set_body(input("Введите тело заметки: "))
        current_date = datetime.date.isoformat(datetime.date.today())
        self.note.set_date(current_date)

        self.save_note(self.note.generate_json(self.notes))

        print("Заметка успешно сохранена!")

    def save_note(self, note_json):
        with open(self.file_name, "w") as f:
            f.write(note_json)
            f.close()

        self.notes = json.loads(note_json)
        self.last_note_id += 1

    def delete_note(self, note_id):
        try:
            del self.notes[note_id]
            self.save_note(json.dumps(self.notes))
            print("Заметка удалена!")
        except:
            print("Заметки с таким id не существует!")

    def edit_note(self, note_id):
        try:
            self.notes[note_id]
            self.note = Note(note_id)

            self.note.set_head(input("Введите заголовок: "))
            self.note.set_body(input("Введите тело заметки: "))
            current_date = datetime.date.isoformat(datetime.date.today())
            self.note.set_date(current_date)

            self.save_note(self.note.generate_json(self.notes))

            print("Заметка успешно отредактирована!")
        except:
            print("Заметки с таким id не существует!")

    def show_note(self, note_id):
        try:
            print("\n", self.notes[note_id]["head"])
            print(" ", self.notes[note_id]["body"])
            print("Дата: ", self.notes[note_id]["date"], "\n")
        except:
            print("Заметки с таким id не существует!")

    def show_all_notes(self):
        notes = []

        for item in self.notes:
            note = tuple()
            note = (item, self.notes[item]["date"])
            notes.append(note)

        for i in range(len(notes)):
            for j in range(i):
                if notes[j][1] > notes[i][1]:
                    tmp = notes[j]
                    notes[j] = notes[i]
                    notes[i] = tmp

        for note in notes:
            print(self.notes[note[0]]["head"])
            print(" ", self.notes[note[0]]["body"])
            print("Дата: ", self.notes[note[0]]["date"])
            print("-----------------\n")
        

            
        

        
