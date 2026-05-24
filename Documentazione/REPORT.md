# 🎰 Report Finale del Progetto: Casino Console
**Autori:** Baffert, Nicodemo, Protti
**Data:** Maggio 2026

## 1. Introduzione e Punto di Partenza
Questo progetto è nato con l'obiettivo di sviluppare un simulatore di casinò testuale basato su terminale utilizzando esclusivamente
Python. 
Siamo partiti da zero con le seguenti idee:
* Creare un'interfaccia utente tramite riga di comando.
* Gestire un sistema di wallet virtuale per l'utente (salvare e aggiornare i gettoni).
* Implementare algoritmi casuali efficaci per simulare il banco dei giochi.

## 2. Architettura e Sviluppo del Codice
Per mantenere il codice pulito e collaborare al meglio con Git  abbiamo diviso il progetto con questo schema modulare:
* `main.py`: Il punto di ingresso del programma che gestisce il menu interattivo principale.
* `Game/`: File e cartelle dedicati alla logica specifica dei singoli giochi.
* `utenti.json`: File utilizzato per la persistenza dei dati, permettendo di salvare il saldo dei giocatori.
* `utils.py`: Funzioni di supporto riutilizzabili per il controllo e la convalida dell'input utente.

## 3. Giochi Implementati e Risultato Finale
Nel codice finale siamo riusciti a integrare con successo tre giochi da tavolo:
1. **🎡 Roulette**: Sistema di puntate su numeri singoli, rosso/nero e pari/dispari.
2. **🎲 Dadi**: Gioco rapido di sfida contro il punteggio del banco.
3. **🃏 Blackjack**: Logica di gioco più complessa con calcolo del punteggio delle carte e opzioni di "carta" o "stai".

## 4. Difficoltà Incontrate e Soluzioni
Durante lo sviluppo abbiamo dovuto affrontare alcuni problemi:
* **Gestione dei bug di input**: Gli utenti inserivano lettere al posto dei numeri per le scommesse. Abbiamo risolto bloccando gli errori in `utils.py` con cicli di controllo.
* **Sincronizzazione dei file**: Lavorando in tre sullo stesso codice, abbiamo imparato a gestire i conflitti di merge su GitHub, dividendo accuratamente le funzioni in file separati.

## 5. Conclusioni e Sviluppi Futuri
Siamo molto soddisfatti del software ottenuto. Rispetta tutti i requisiti stabiliti all'inizio del lavoro.
In futuro il progetto potrebbe essere ampliato aggiungendo un sistema multiplayer locale.
