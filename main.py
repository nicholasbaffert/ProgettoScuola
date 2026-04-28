from utils import clear, login_o_registrazione, aggiorna_saldo_utente
import time

def main():
    clear()
    print("=== BENVENUTO AL CASINO CONSOLE ===")
    username, saldo = login_o_registrazione()
    time.sleep(1.5)

    while True:
        clear()
        print(f"--- Utente: {username} - Saldo: {saldo}€ ---")  
        print("1) Roulette 🎡")
        print("2) Dadi 🎲")
        print("3) Blackjack 🃏")
        print("4) Statistiche (Coming Soon)")
        print("5) Esci")
        try:
            scelta = int(input("\nInserisci Scelta (1-5): "))

        except ValueError:
            print("Inserisci un numero valido!")
            time.sleep(1)
            continue

        if scelta == 1:
            print("Avvio Roulette...")
            time.sleep(1)
        
        elif scelta == 2:
            print("Avvio Sfida dei Dadi...")
            puntata = 10
            if saldo >= puntata:
                saldo = saldo - puntata
                aggiorna_saldo_utente(username, saldo)
            else:
                print("Saldo insufficiente!")
            time.sleep(1)

        elif scelta == 5:
            print(f"Salvataggio dati... Grazie per aver giocato, {username}!")
            aggiorna_saldo_utente(username, saldo)
            break
        
        else:
            print("Scelta non valida")
            time.sleep(1)

if __name__ == "__main__":
    main()