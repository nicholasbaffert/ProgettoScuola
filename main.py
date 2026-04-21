from utils import clear
import time

def main():
    while True:
        clear()
        print("=== 3M: Quiz & Mini-Game ===")
        print("1) Gioca al quiz")
        print("2) Sfida dei dadi")
        print("3) Raccontami una barzelletta")
        print("4) Statistiche")
        print("5) Esci")

        scelta:int=int(input("Inserisci Scelta: (1-5)")) 
        if scelta < 1 or scelta > 6:
            print()
            print("Scelta non valida")
            print()
            time.sleep(0.5)
            continue

            
if __name__ == '__main__':
    main()

