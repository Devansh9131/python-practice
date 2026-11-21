import os


def add_note():
    note = input("Enter your note: ")

    if note.strip() == "":
        print("Please enter a note.\n")
        return
    with open("notes.txt", "a") as f:
        f.write(f"{note}\n")

    print("Note saved.\n")


def view_notes():
    if os.path.exists("notes.txt"):
        with open("notes.txt") as f:
            notes = f.read()

            if notes.strip() == "":
                print("No notes yet.\n")
                return

            notes = notes.strip().split("\n")

            for index, line in enumerate(notes, 1):
                print(index, line)
            print()
    else:
        print("No notes yet.\n")


def menu():
    while True:

        print("1. Add a note\n2. View notes\n3. Exit")

        choice = input("Enter a choice: ").strip()

        match choice:
            case "1":
                add_note()
            case "2":
                view_notes()
            case "3":
                print("Goodbye!")
                return
            case _:
                print("Invalid choice.\n")


menu()
