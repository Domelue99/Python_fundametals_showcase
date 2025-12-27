import os
from pathlib import Path
#TASK_FILE = "tasks.txt"
MAIN_DIRECTORY = "Database/"

def load_directory():
    if not os.path.isdir(MAIN_DIRECTORY):
        return[]
    
    directories = []
    
    for file in Path (MAIN_DIRECTORY).iterdir():
        if file.is_file() and file.suffix == ".txt":
            directories.append(file.stem)
        
    return directories

def load_task(directory_name):
    if not os.path.exists(directory_name):
        return[]
    with open(directory_name) as file:
        return[line.strip() for line in file.readlines()]
    
def save_task(directory_name, tasks):
    with open("Database/" + directory_name, "w") as file:
        for task in tasks:
            file.write(task +"\n")

def show_menu():
    print("\n=== Hauptmenü ===")
    print("1. Ordner auswählen")
    print("2. Ordner hinzufügen")
    print("3. Ordner löschen")
    print("4. Beenden")

def show_menu_tasks(directory: list[str], number: int) -> None:
    if not isinstance(directory, list):
        raise TypeError("directory muss eine Liste sein")
    if not isinstance(number, int):
        raise TypeError("number muss int sein")
    if number < 0 or number >= len(directory):
        raise IndexError("Ungültige Auswahl")
    tasks = load_task("Database/" + directory[number] +".txt")
    while True:
        print("\n=== " + directory[number] + " ===")
        print("1. Aufgaben anzeigen")
        print("2. Aufgabe hinzufügen")
        print("3. Aufgabe löschen")
        print("4. Zurück zum Hauptmenü")
        choice = input("Eingabe: ")
        if choice == "1":
            show_task(tasks)
        elif choice == "2":
            add_task(tasks)
            save_task(directory[number]+".txt", tasks)
        elif choice == "3":
            delete_task(tasks)
            save_task(directory[number]+".txt", tasks)
        elif choice == "4":
            break
        else:
            print("Falsche Eingabe")

def show_directory(directories: list[str])-> None :

    if not directories:
        print("\nKeine Ordner gefunden")
    else:
        directories.sort()
        print("\nAktuelle Ordner:")
        for i, directory in enumerate(directories,1):
            print(f"{i}. {directory}")
        
        number = int(input("Ordner auswählen: ") ) -1 
        
        show_menu_tasks(list(directories), int(number))

def sort_directories(directories: list[str])->None:
    directories.sort()

def add_directory(directories):
    
    while True:
        check = False
        new_directory = input("Ordnername: ")

        for directory in directories:
            if new_directory == directory:
                print("Name bereits vergegben!")
                check = True
            
            if len(directories) >= 10 :
                print("Zu viele Ordner, bitte Ordner löschen um neuen Ordner zu erstellen!")
                break

        if not check:
            directories.append(new_directory)
            from pathlib import Path

            path = Path("Database/" + new_directory + ".txt")
            path.touch(exist_ok=False)
            break



def show_task(tasks):

    if not tasks:
        print("\nKeine Aufgaben gefunden")
    else:
        print("\nAktuelle Aufgaben:")
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task}")

def add_task(tasks):
    new_task = input("Neue Aufgabe: ")
    tasks.append(new_task)
    print("Aufgabe hinzugefügt!")


def delete_task(tasks):
    show_task(tasks)
    try:
        number = int(input("Welche Aufgabe soll gelöscht werden? "))
        tasks.pop(number-1)
        print("Aufgabe gelöscht")

    except(ValueError,IndexError):
        print("Eingabe ungültig")

def main():
    directory = list(load_directory())
    

    while True:
        show_menu()
        choice = input("Triff eine Auswahl: ")

        if choice == "1":
            show_directory(directory)
        elif choice == "2":
            add_directory(directory)
        elif choice == "3":
            delete_directory(directory)
        elif choice == "4":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe!")


if __name__ == "__main__":
    main()


