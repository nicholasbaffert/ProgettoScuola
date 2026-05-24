# 🎰 Casino Gold Premium

## 📌 Descrizione
**Casino Gold Premium** è un simulatore di casinò interattivo con interfaccia grafica moderna realizzato in Python.

L'utente può:
- Registrarsi e effettuare il login
- Giocare a tre giochi diversi (Roulette, Dadi, Blackjack)
- Gestire un saldo virtuale da 1000€
- Visualizzare grafici statistici dell'andamento del proprio capitale
- Tracciare la cronologia di tutte le giocate

---

## 🎯 Caratteristiche Principali

### 🎮 Giochi Disponibili
- **🎡 Roulette**: Puntate su numeri, rosso/nero, pari/dispari con vincite fino a 36x
- **🎲 Dadi**: Lanciare due dadi (costo 10€, premio 25€ se somma > 7)
- **🃏 Blackjack**: Arrivare a 21 senza superarlo, con strategia del banco

### 💻 Interfaccia
- Tema scuro elegante (#1a1a1a) con accenti dorati (#ffd700)
- Login/registrazione automatica con persistenza dati
- Menu principale intuitivo
- Grafici dell'andamento del saldo

### 📊 Statistiche
- Cronologia completa di ogni giocata
- Grafico interattivo del saldo nel tempo

---

## 🚀 Come Iniziare

### Prerequisiti
- Python 3.7+
- pip (gestore pacchetti Python)

### Installazione

1. **Vai nella cartella del progetto**
   ```bash
   cd Casino-Project
   ```

2. **Installa le dipendenze** (doppio-click su questo file):
   ```
   install_dependencies.bat
   ```
   Oppure da terminale:
   ```bash
   pip install -r requirements.txt
   ```

3. **Avvia il programma**
   ```bash
   python main.py
   ```

---

## 📁 Struttura del Progetto

```
Casino-Project/
├── main.py                          # Applicazione principale
├── requirements.txt                 # Dipendenze
├── install_dependencies.bat         # Installa automaticamente
├── utenti.json                      # Database (creato automaticamente)
├── README.md                        # Questo file
├── LICENSE                          # Licenza MIT
│
├── Game/
│   ├── __init__.py
│   ├── roulette.py                 # Logica della Roulette
│   ├── dadi.py                     # Gioco dei Dadi
│   └── blackjack.py                # Logica del Blackjack
│
└── Documentazione/
    ├── Documento_Requisiti.md      # Specifica tecnica completa
    ├── REPORT.md                   # Relazione finale
    └── Gantt/                      # Diagrammi
```

---

## 📋 Requisiti Funzionali

✅ Sistema di login/registrazione
✅ Tre giochi interattivi con GUI
✅ Gestione saldo virtuale (1000€)
✅ Salvataggio persistente su JSON
✅ Cronologia giocate
✅ Grafici matplotlib
✅ Tema dark coordinato
✅ Gestione errori robusta

---

## 📦 Dipendenze

- **tkinter** (incluso) - Interfaccia grafica
- **matplotlib** - Grafici statistici
- **json** (built-in) - Persistenza dati
- **random** (built-in) - Numeri casuali
- **os** (built-in) - Gestione file

---

## 🔐 Persistenza Dati

I dati degli utenti vengono salvati in `utenti.json` con la seguente struttura:

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

---

## 📝 Licenza

Questo progetto è distribuito sotto licenza MIT.

---

## 👨‍💻 Autori

- **Baffert** - Roulette, GUI principale, integrazione
- **Nicodemo** - Dadi, sistema di saldo
- **Protti** - Blackjack, statistiche

Maggio 2026
