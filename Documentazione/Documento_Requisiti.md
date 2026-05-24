# 🎰 Documento dei Requisiti  
## Progetto: Casino Console – Mini Gambling Games

---

## ⚙️ REQUISITI DI INSTALLAZIONE (DA LEGGERE PRIMA)

### 📦 Dipendenze richieste:
- **Python 3.7+**
- **matplotlib** (per i grafici statistici)
- **tkinter** (incluso in Python per impostazione predefinita)

### 🚀 Installazione automatica:
**Esegui il file `install_dependencies.bat` per installare automaticamente tutte le dipendenze.**

Altrimenti, da terminale:
```
pip install -r requirements.txt
```

---

## 1. 📌 Titolo del progetto
Casino Gold Premium – Mini Gambling Games GUI

---

## 2. 🎯 Obiettivo
Il progetto implementa un casinò con **interfaccia grafica moderna (GUI con tkinter)**, con tema scuro e design elegante.

L'utente può:
- Effettuare il login o registrarsi
- Giocare a diversi giochi d'azzardo virtuali
- Gestire il proprio saldo
- Visualizzare statistiche personali tramite grafici
- Tenere traccia della cronologia delle giocate


## 3. 👥 Attori
- Utente / Giocatore  
- Sistema (applicazione console)

---

## 4. ⚙️ Requisiti funzionali
Il sistema deve:
- Fornire un'interfaccia grafica moderna con tema scuro e dorato
- Gestire il login/registrazione degli utenti
- Consentire la scelta tra i giochi:
  - **Roulette** (finestra dedicata)
  - **Dadi** (minigioco istantaneo)
  - **Blackjack** (finestra dedicata)
- Gestire un saldo iniziale del giocatore (1000€)
- Permettere di effettuare puntate in ogni gioco
- Generare risultati casuali tramite random
- Calcolare vincite e perdite automaticamente
- Aggiornare il saldo in tempo reale
- Bloccare puntate superiori al saldo disponibile
- Salvare i dati dell'utente e cronologia su file JSON
- Mostrare grafici statistici dell'andamento del saldo
- Visualizzare l'esito di ogni partita
- Permettere il ritorno al menu principale o l'uscita dal gioco
- Tracciare la cronologia di ogni giocata (gioco, variazione saldo, saldo finale)

---

## 5. 🧱 Requisiti non funzionali
- Interfaccia grafica moderna e intuitiva
- Tema scuro (#1a1a1a) con accenti dorati (#ffd700)
- Codice modulare in file separati
- Gestione robusta degli errori:
  - input non valido
  - valori fuori range
  - puntate errate
  - salvataggio dati corrotto
- Salvataggio persistente su file JSON
- Grafici statistici con matplotlib
- Codice ben commentato e mantenibile
- Esecuzione stabile senza crash

---

## 6. 🎮 Logica dei giochi

### 🎡 Roulette
- Interfaccia dedicata in finestra separata
- Numeri da 0 a 36
- Puntate disponibili:
  - Rosso/Nero → x2
  - Pari/Dispari → x2
  - Numero secco → x36
- Risultato casuale generato al click

---

### 🎲 Dadi
- Minigioco istantaneo dal menu principale
- Costo fisso: 10€ per giocata
- 2 dadi virtuali (1–6)
- Regola:
  - Vittoria → +25€ (guadagno netto: +15€)
  - Sconfitta → -10€
- Mostra il risultato in popup

---

### 🃏 Blackjack
- Interfaccia dedicata in finestra separata
- Implementato dai compagni di progetto
- Obiettivo: arrivare a 21 senza superarlo
- Azioni disponibili:
  - **HIT** → pesca una carta
  - **STAND** → termina il turno
- Valore delle carte:
  - numeri → valore nominale (2-10)
  - figure (J, Q, K) → 10
  - asso → 1 o 11 (a scelta del giocatore)
- Esiti:
  - 21 con due carte → Blackjack (vittoria)
  - più vicino a 21 del banco → vittoria
  - uguali al banco → pareggio
  - supera 21 → sconfitta (bust)

---

## 7. 💰 Sistema di saldo
- **Saldo iniziale**: 1000€ per ogni nuovo utente
- **Saldo recupero**: Se l'utente è già registrato, il suo saldo viene ripristinato
- Ogni puntata viene sottratta dal saldo
- Le vincite vengono aggiunte al saldo
- Se saldo < costo del gioco → puntata bloccata
- Se saldo = 0 → il giocatore continua comunque (nessun Game Over forzato)
- Tutti i movimenti vengono salvati in cronologia

---

## 8. 📁 Struttura del progetto
```
Casino-Project/
│
├── main.py                           # Applicazione principale (GUI)
├── utenti.json                       # Database degli utenti (creato automaticamente)
├── requirements.txt                  # Dipendenze Python
├── install_dependencies.bat          # Script automatico per installare dipendenze
│
├── Game/
│   ├── __init__.py
│   ├── roulette.py                   # Logica della Roulette
│   ├── dadi_tkinter.py               # Minigioco dei Dadi
│   └── blackjack.py                  # Logica del Blackjack
│
└── Documentazione/
    ├── Documento_Requisiti.md        # Questo file
    └── Gantt/
```

---

## 9. 🔁 Flusso del programma
```
Avvio programma (main.py)
↓
Finestra Login / Registrazione
↓
Menu Principale (Roulette, Dadi, Blackjack, Statistiche, Esci)
↓
Scelta gioco
│
├─ Roulette → Finestra dedicata
├─ Dadi → Minigioco istantaneo
├─ Blackjack → Finestra dedicata
└─ Statistiche → Grafico matplotlib
↓
Aggiornamento saldo
↓
Salvataggio dati (JSON)
↓
Ritorno al Menu Principale
↓
Uscita (destroy)
```

---

## 10. ⚠️ Gestione errori
- Username vuoto → avviso popup e reinserimento
- Saldo insufficiente → blocco della puntata con messagebox
- File JSON corrotto → ricreazione automatica del file vuoto
- Import falliti → segnalazione d'errore con exit
- Grafici con pochi dati → messaggio informativo "Effettua almeno una puntata"

---

## 11. 🚀 Estensioni future
- Salvataggio del saldo su database (SQLite/MySQL)
- Ranking globale (classifica top players)
- Animazioni grafiche nei giochi
- Effetti sonori
- Tema selezionabile (chiaro/scuro)
- Nuovi giochi (Poker, Slots, Baccarat)
- Modalità multiplayer locale o online
- Export statistiche in PDF/Excel
- Protezione account con password
- Bonus giornalieri e promozioni

---

## 12. 📅 Cronoprogramma
- Settimana 1 → Idealizzazione progetto/creazione file
- Settimana 2 → Sviluppo vari giochi
- Settimana 3 → Unificazione dei giochi in un menu
- Settimana 4 → Controllo bugs e consegna progetto

---

## 13. 📦 Package utilizzati

### Standard Library (inclusi in Python):
- **os** → gestione file e directory
- **json** → salvataggio/caricamento dati utenti
- **random** → generazione numeri casuali per i giochi

### Dipendenze esterne:
- **tkinter** → interfaccia grafica (incluso in Python)
- **matplotlib** → grafici statistici dell'andamento del saldo

### Da installare:
- Vedi la sezione "REQUISITI DI INSTALLAZIONE" all'inizio di questo documento


## 14. 📊 Funzionalità Statistiche
- **Grafico andamento saldo**: mostra l'evoluzione del capitale nel tempo
- **Cronologia giocate**: registra ogni partita con:
  - Nome del gioco
  - Variazione saldo (+/-)
  - Saldo finale dopo la giocata
- **Annotazioni giochi**: ogni punto del grafico è etichettato con il nome del gioco
- **Tema coordinato**: il grafico rispetta il tema scuro dell'applicazione
- **Protezione dati**: i grafici vengono generati solo se ci sono almeno 2 dati

## 15. 🎨 Interfaccia Grafica (Tema Dark Premium)
- **Colore sfondo principale**: #1a1a1a (nero elegante)
- **Colore panelli**: #262626 (grigio scuro)
- **Colore accento**: #ffd700 (oro lucido)
- **Colore testo**: #ffffff (bianco) e #b3b3b3 (grigio chiaro)
- **Font**: Helvetica per titoli e testi, Georgia per sottotitoli
- **Effetti**: hover su bottoni, bordi dorati su panel, cursore hand2 su pulsanti

## 16. 🔐 Persistenza Dati
- **File database**: `utenti.json`
- **Formato**: JSON con struttura per utente:
  ```json
  {
    "username": {
      "saldo": 1000,
      "cronologia": [
        {
          "gioco": "Roulette",
          "variazione": 50,
          "saldo_risultante": 1050
        }
      ]
    }
  }
  ```
- **Creazione automatica**: se il file non esiste, viene creato al primo login
- **Backup automatico**: salvataggio dopo ogni giocata

## 14. Gannt/Flowchart
<img width="1688" height="331" alt="Screenshot 2026-05-19 113136" src="https://github.com/user-attachments/assets/03a67268-f53a-4888-8762-ce4f02126b36" />



<img width="1920" height="527" alt="Screenshot 2026-05-07 124722" src="https://github.com/user-attachments/assets/f1f36983-536f-48dc-8bfc-62032cdba60e" />

---

## ⚖️ Nota finale
Il progetto è puramente educativo e non utilizza denaro reale.
