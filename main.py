from application import Application

app = Application("notes.json")

is_exit = False
while not is_exit:
    command = input("Введите команду: ")

    if command == "/q":
        is_exit = True
    else:
        app.command(command)