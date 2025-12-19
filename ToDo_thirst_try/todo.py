import os

TASK_FILE = "tasks.txt"

def load_tasks():
    """Lädt vorhandene Aufgaeben aus der Datei."""
    if not os.path.exists(TASK_FILE):
        return[]
    with open(TASK_FILE) as file:   
        return [line.strip() for line in file.readlines()]
    #der with operator öffnet die Datei und schließt sie wieder sauber. 
    #wenn bei der alternative auftritt, wird die Datei eventuell nicht sauber aufgeräumt/geschlossen
    #f = open(...)
    #lines = f.readlines()
    #f.close()

def save_tasks(tasks):
    """Speichert Aufgaben in der Datei."""
    with open(TASK_FILE,"w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n==== To-Do-Liste ====")
    print("1. Aufgaben anzeigen")
    print("2. Aufgaben hinzufügen")
    print("3. Aufgaben löschen")
    print("4. Beenden")

def show_tasks(tasks):
    if not tasks:
        print("\nKeine Aufgaben vorhanden")

    else:
        print("\nAktuelle Aufgaben:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_tasks(tasks):
    new_task = input("Neue Aufgabe: ")
    tasks.append(new_task)
    print("Aufgabe Hinzugefügt!")

def delete_tasks(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Nummer der gelöschten Aufgabe: "))
        tasks.pop(number - 1)
        print("Aufgabe gelöscht!")
    except (ValueError, IndexError):
        print("Ungültige eingabe!")

    
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Auswahl: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
            save_tasks(tasks)
        elif choice == "3":
            delete_tasks(tasks)
        elif choice == "4":
            print("Programm beenden")
            break
        else:
            print("Ungültige eingabe!")

if __name__ == "__main__":
    main()


            