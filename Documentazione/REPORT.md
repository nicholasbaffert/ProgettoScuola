# 🎰 Report Finale del Progetto: Casino Gold Premium
**Autori:** Baffert, Nicodemo, Protti
**Data:** Maggio 2026

## 1. Introduzione e Punto di Partenza
Questo progetto è nato con l'obiettivo di sviluppare un simulatore di casinò con interfaccia grafica moderna utilizzando Python.
Siamo partiti da zero con le seguenti idee:
* Creare un'interfaccia utente elegante e intuitiva tramite tkinter.
* Gestire un sistema di login/registrazione per gli utenti.
* Implementare un sistema di wallet virtuale con persistenza su file JSON.
* Sviluppare grafici statistici per tracciare l'andamento del saldo nel tempo.
* Implementare algoritmi casuali efficaci per simulare i giochi.

## 2. Architettura e Sviluppo del Codice
Per mantenere il codice pulito e collaborare al meglio con Git, abbiamo diviso il progetto con questo schema modulare:
* `main.py`: Il punto di ingresso del programma che gestisce l'interfaccia grafica principale (login, menu, grafica statistica).
* `Game/`: Cartella contenente la logica specifica dei singoli giochi (roulette.py, blackjack.py, dadi.py).
* `utenti.json`: File utilizzato per la persistenza dei dati, permettendo di salvare il saldo e la cronologia dei giocatori.
* `requirements.txt`: Specifica le dipendenze esterne (matplotlib).
* `install_dependencies.bat`: Script di installazione automatica per le dipendenze.

## 3. Giochi Implementati e Risultato Finale
Nel codice finale siamo riusciti a integrare con successo tre giochi con interfaccia dedicata:
1. **🎡 Roulette**: Finestra dedicata con sistema di puntate su numeri singoli, rosso/nero e pari/dispari.
2. **🎲 Dadi**: Gioco dei dadi con logica di vittoria/sconfitta (somma > 7 = vittoria).
3. **🃏 Blackjack**: Logica di gioco complessa con calcolo del punteggio delle carte e opzioni di "hit" o "stand".

## 4. Difficoltà Incontrate e Soluzioni
Durante lo sviluppo abbiamo dovuto affrontare alcuni problemi:
* **Gestione della concorrenza tra finestre**: Inizialmente avevamo problemi con la sincronizzazione del saldo tra finestre diverse. Abbiamo risolto implementando callback functions che aggiornano main.py al termine di ogni gioco.
* **Persistenza dati e cronologia**: Dovevamo salvare la cronologia delle giocate per generare grafici. Abbiamo implementato un sistema JSON strutturato che traccia ogni movimento.
* **Integrazione con codice dei compagni**: Dovevamo integrare il blackjack.py fatto dai compagni con il nostro main. Abbiamo creato una funzione `start_game()` standard per tutti i giochi.

## 5. Conclusioni e Sviluppi Futuri
Siamo molto soddisfatti del software ottenuto. Rispetta tutti i requisiti stabiliti all'inizio del lavoro e offre un'esperienza utente piacevole con tema dark elegante.
In futuro il progetto potrebbe essere ampliato aggiungendo:
* Database SQLite per migliore persistenza
* Sistema di ranking tra gli utenti
* Nuovi giochi (Poker, Slots, Baccarat)
* Modalità multiplayer locale
* Temi selezionabili
