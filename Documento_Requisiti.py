# ==========================================================
# 🎰 DOCUMENTO DEI REQUISITI
# Progetto: Casino Console – Mini Gambling Games
# ==========================================================


# ----------------------------------------------------------
# 1. TITOLO DEL PROGETTO
# ----------------------------------------------------------
# Casino Console – Mini Gambling Games


# ----------------------------------------------------------
# 2. OBIETTIVO
# ----------------------------------------------------------
# Il programma offre un sistema a console che permette
# all’utente di simulare un’esperienza da casino.
# Include giochi come roulette, dadi e slot machine,
# con gestione del saldo e delle puntate.


# ----------------------------------------------------------
# 3. ATTORI
# ----------------------------------------------------------
# - Utente / Giocatore
# - Sistema (app console)


# ----------------------------------------------------------
# 4. REQUISITI FUNZIONALI
# ----------------------------------------------------------
# Il sistema deve:
#
# - Avviare un menu principale interattivo
# - Consentire la scelta tra più giochi:
#     • Roulette
#     • Dadi
#     • Slot machine (opzionale)
# - Gestire un saldo iniziale del giocatore
# - Permettere all’utente di:
#     • effettuare puntate
#     • scegliere il tipo di scommessa
# - Generare risultati casuali (modulo random)
# - Calcolare vincite e perdite
# - Aggiornare il saldo in tempo reale
# - Impedire puntate superiori al saldo
# - Mostrare messaggi di vittoria/sconfitta
# - Consentire di tornare al menu o uscire


# ----------------------------------------------------------
# 5. REQUISITI NON FUNZIONALI
# ----------------------------------------------------------
# - Interfaccia a console chiara e leggibile
# - Codice modulare e organizzato:
#     • main.py → menu e flusso principale
#     • roulette.py → logica roulette
#     • dice.py → gioco dadi
#     • slot.py → slot machine (opzionale)
#     • utils.py → funzioni di supporto
# - Gestione errori:
#     • input non validi
#     • valori fuori range
# - Codice commentato e comprensibile
# - Esecuzione veloce e senza blocchi


# ----------------------------------------------------------
# 6. LOGICA DI GIOCO
# ----------------------------------------------------------

# 🎡 ROULETTE
# - Numeri da 0 a 36
# - Tipi di puntata:
#     • Rosso/Nero → payout x2
#     • Pari/Dispari → payout x2
#     • Numero secco → payout x35

# 🎲 DADI
# - Lancio di 2 dadi (1–6)
# - Regole base:
#     • Somma > 7 → vittoria
#     • Somma ≤ 7 → sconfitta

# 🎰 SLOT MACHINE (opzionale)
# - 3 simboli casuali
# - Combinazioni:
#     • 3 uguali → grande vincita
#     • 2 uguali → piccola vincita


# ----------------------------------------------------------
# 7. GESTIONE SALDO
# ----------------------------------------------------------
# - Saldo iniziale (es. 100)
# - Ogni puntata viene sottratta
# - Vincite aggiunte al saldo
# - Se saldo = 0 → fine gioco (Game Over)


# ----------------------------------------------------------
# 8. STRUTTURA DEL PROGETTO
# ----------------------------------------------------------
#
# casino_project/
# │
# ├── main.py
# ├── roulette.py
# ├── dice.py
# ├── slot.py
# ├── utils.py
# └── README.md
#


# ----------------------------------------------------------
# 9. FLUSSO DEL PROGRAMMA
# ----------------------------------------------------------
#
# Avvio programma
# ↓
# Menu principale
# ↓
# Scelta gioco
# ↓
# Inserimento puntata
# ↓
# Esecuzione gioco
# ↓
# Aggiornamento saldo
# ↓
# Mostra risultato
# ↓
# Ritorno al menu o uscita
#


# ----------------------------------------------------------
# 10. GESTIONE ERRORI
# ----------------------------------------------------------
# - Bloccare input non numerici
# - Impedire puntate negative o superiori al saldo
# - Richiedere reinserimento dati


# ----------------------------------------------------------
# 11. ESTENSIONI FUTURE
# ----------------------------------------------------------
# - Salvataggio saldo su file
# - Sistema livelli
# - Statistiche (win/loss)
# - Interfaccia grafica (tkinter)
# - Colori in console (colorama)
# - Multiplayer locale


# ----------------------------------------------------------
# 12. CRONOPROGRAMMA
# ----------------------------------------------------------
# Settimana 1 → progettazione e requisiti
# Settimana 2 → menu + gestione saldo
# Settimana 3 → sviluppo giochi
# Settimana 4 → test e miglioramenti


# ==========================================================
# FINE DOCUMENTO
# ==========================================================
