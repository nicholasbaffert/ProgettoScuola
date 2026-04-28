# 🎰 Documento dei Requisiti  
## Progetto: Casino Console – Mini Gambling Games

---

## 1. 📌 Titolo del progetto
Casino Console – Mini Gambling Games

---

## 2. 🎯 Obiettivo
Il programma simula un piccolo casinò in console.

L’utente può giocare a diversi mini-giochi, effettuare puntate e gestire un saldo virtuale.

Il progetto serve per esercitarsi con:
- programmazione in Python
- logica dei giochi
- gestione input/output
- strutturazione modulare del codice

---

## 3. 👥 Attori
- Utente / Giocatore
- Sistema (applicazione console)

---

## 4. ⚙️ Requisiti funzionali

Il sistema deve:

- Avviare un menu principale interattivo
- Consentire la scelta tra i giochi:
  - 🎡 Roulette
  - 🎲 Dadi
  - 🃏 Blackjack
- Gestire un saldo iniziale del giocatore
- Permettere di effettuare puntate
- Gestire decisioni di gioco (es. hit / stand nel blackjack)
- Generare risultati casuali (random)
- Calcolare vincite e perdite
- Aggiornare il saldo in tempo reale
- Bloccare puntate superiori al saldo disponibile
- Mostrare esito di ogni partita
- Permettere di tornare al menu o uscire

---

## 5. 🧱 Requisiti non funzionali

- Interfaccia testuale chiara e leggibile
- Codice modulare e separato in file:
  - `main.py` → menu e flusso principale
  - `roulette.py` → logica roulette
  - `dice.py` → gioco dadi
  - `blackjack.py` → logica blackjack
  - `utils.py` → funzioni di supporto
- Gestione robusta degli errori:
  - input non valido
  - valori fuori range
- Codice commentato e comprensibile
- Esecuzione veloce senza blocchi

---

## 6. 🎮 Logica dei giochi

### 🎡 Roulette
- Numeri da 0 a 36
- Tipi di puntata:
  - Rosso/Nero → x2
  - Pari/Dispari → x2
  - Numero singolo → x35

---

### 🎲 Dadi
- Lancio di 2 dadi (1–6)
- Regola base:
  - Somma > 7 → vittoria
  - Somma ≤ 7 → sconfitta

---

### 🃏 Blackjack
- Obiettivo: arrivare il più vicino possibile a 21 senza superarlo
- Azioni:
  - hit → pescare carta
  - stand → fermarsi
- Valori carte:
  - numeri → valore nominale
  - figure → 10
  - asso → 1 o 11
- Risultati:
  - >21 → sconfitta (bust)
  - migliore del banco → vittoria
  - uguale → pareggio

---

## 7. 💰 Sistema di saldo

- Saldo iniziale (es. 100)
- Ogni puntata viene sottratta
- Le vincite vengono aggiunte al saldo
- Se saldo = 0 → Game Over

---

## 8. 📁 Struttura del progetto
