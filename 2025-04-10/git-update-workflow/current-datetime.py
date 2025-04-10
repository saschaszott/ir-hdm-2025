from datetime import datetime

def main():
    now = datetime.now()
    # Kommentar vom Dozenten
    print("Aktuelle Systemzeit:", now.strftime("%H:%M:%S"))
    print("Aktuelles Datum:", now.strftime("%Y-%m-%d")) # <-- neue Zeile hinzugefügt

if __name__ == "__main__":
    main()
