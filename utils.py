import os
import json

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

DB_FILE = "users.json"

def carica_dati():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def salva_dati(dati):
    with open(DB_FILE, "w") as f:
        json.dump(dati, f, indent=4)

def login_o_registrazione():
    dati = carica_dati()
    username = input("Inserisci il tuo username: ").strip().lower()

    if username in dati:
        print(f"Bentornato {username}! Saldo attuale: {dati[username]}€")
        return username, dati[username]
    else:
        print("Nuovo utente rilevato. Creazione account...")
        saldo_iniziale = 100
        dati[username] = saldo_iniziale
        salva_dati(dati)
        print(f"Benvenuto {username}! Ti sono stati accreditati {saldo_iniziale}€.")
        return username, saldo_iniziale

def aggiorna_saldo_utente(username, nuovo_saldo):
    dati = carica_dati()
    dati[username] = nuovo_saldo
    salva_dati(dati)