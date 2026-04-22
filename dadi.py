import random
import time

def animazione_lancio():
    print("\n🎲 Sto lanciando il dado...")
    for i in range(5):
        print("...")
        time.sleep(0.3)

def lancia_dado():
    animazione_lancio()
    risultato = random.randint(1, 6)
    print(f"👉 Il dado ha mostrato: {risultato}")
    return risultato

def mostra_storico(storico):
    print("\n📜 Storico dei lanci:")
    for i, valore in enumerate(storico, start=1):
        print(f"Tentativo {i}: {valore}")

def mostra_statistiche(tentativi, vittorie):
    print("\n📊 STATISTICHE:")
    print(f"- Tentativi totali: {tentativi}")
    print(f"- Vittorie: {vittorie}")
    
    if tentativi > 0:
        percentuale = (vittorie / tentativi) * 100
        print(f"- Percentuale di vittoria: {percentuale:.2f}%")

def gioco():
    print("=== 🎮 GIOCO DEL DADO ===")
    print("Regola: fai 6 per vincere!\n")

    tentativi = 0
    vittorie = 0
    storico = []

    while True:
        scelta = input("\nVuoi lanciare il dado? (s/n/stat): ").lower()

        if scelta == "s":
            tentativi += 1
            risultato = lancia_dado()
            storico.append(risultato)

            print(f"🎯 Tentativo numero: {tentativi}")

            if risultato == 6:
                print("🎉 GRANDISSIMO! Hai fatto 6!")
                vittorie += 1
            else:
                print("😢 Niente 6... riprova!")

        elif scelta == "stat":
            mostra_statistiche(tentativi, vittorie)
            mostra_storico(storico)

        elif scelta == "n":
            print("\n👋 Fine gioco!")
            mostra_statistiche(tentativi, vittorie)
            break

        else:
            print("❌ Scelta non valida! Scrivi 's', 'n' oppure 'stat'.")

if __name__ == "__main__":
    gioco()

