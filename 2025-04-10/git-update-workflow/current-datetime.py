from datetime import datetime

def main():
    """
    Diese Funktion gibt die aktuelle Systemzeit und das aktuelle Datum aus.
    """
    now = datetime.now()
    # ein Kommentar, der vom Dozenten eingefügt wurde <-- weitere Änderung
    print("Aktuelle Systemzeit:", now.strftime("%H:%M:%S"))
    print("Aktuelles Datum:", now.strftime("%Y-%m-%d")) # <-- neue Zeile hinzugefügt

if __name__ == "__main__":
    main()