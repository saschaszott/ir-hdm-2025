from datetime import datetime

def main():
    """
    Diese Funktion gibt die aktuelle Systemzeit.
    Es wird kein Argument erwartet.
    """
    now = datetime.now()    
    print("Aktuelle Systemzeit:", now.strftime("%H:%M:%S"))    

if __name__ == "__main__":
    main()