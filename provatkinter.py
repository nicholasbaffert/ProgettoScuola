import tkinter as tk
from tkinter import messagebox
import math
import random

# --- CLASSE GIOCO ROULETTE ---
class Roulette:
    def __init__(self, parent, budget_iniziale, callback_chiusura):
        # Crea una finestra secondaria (Toplevel) che sta sopra quella principale
        self.window = tk.Toplevel(parent)
        self.window.title("3M Roulette")
        self.window.geometry("900x700") # Dimensione della finestra
        self.window.configure(bg="#1a1a1a") # Colore di sfondo grigio scuro

        # Variabili di gioco
        self.budget = budget_iniziale
        self.callback = callback_chiusura # Funzione per "parlare" col menu principale
        self.puntate = {} # Dizionario per salvare le scommesse (es: {5: 100})
        self.numeri = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
        self.angolo = 0 # Posizione attuale della pallina in gradi
        self.in_corso = False # Diventa True quando la ruota gira

        self.setup_interfaccia()

    def setup_interfaccia(self):
        # Titolo e Budget in alto
        self.lbl_budget = tk.Label(self.window, text=f"Budget: €{self.budget}", font=("Arial", 18), bg="#1a1a1a", fg="gold")
        self.lbl_budget.pack(pady=10)

        # Creazione della tela (Canvas) per disegnare la roulette
        self.canvas = tk.Canvas(self.window, width=400, height=400, bg="#1a1a1a", highlightthickness=0)
        self.canvas.pack()
        
        # Disegno dei numeri sulla ruota
        cx, cy = 200, 200 # Centro del canvas
        for i, num in enumerate(self.numeri):
            # Calcolo dell'angolo per ogni spicchio (360 gradi divisi per 37 numeri)
            rad = math.radians(i * (360/37) - 90)
            x, y = cx + 160 * math.cos(rad), cy + 160 * math.sin(rad)
            # Disegna un cerchietto colorato per ogni numero
            col = "green" if num == 0 else ("red" if i%2==0 else "black")
            self.canvas.create_oval(x-12, y-12, x+12, y+12, fill=col)
            self.canvas.create_text(x, y, text=str(num), fill="white", font=("Arial", 8))

        # Disegno della pallina (inizialmente invisibile al centro)
        self.pallina = self.canvas.create_oval(0, 0, 0, 0, fill="white")

        # Zona scommesse (Bottoni per puntare)
        frame_bet = tk.Frame(self.window, bg="#1a1a1a")
        frame_bet.pack(pady=20)
        
        # Esempio: puntata fissa da 100€ su alcuni numeri
        for n in [0, 10, 20, 30]:
            tk.Button(frame_bet, text=f"Punta su {n}", command=lambda x=n: self.scommetti(x)).pack(side="left", padx=5)

        # Bottone per avviare il giro
        self.btn_gira = tk.Button(self.window, text="GIRA!", font=("Arial", 14, "bold"), bg="gold", command=self.avvia_gioco)
        self.btn_gira.pack(pady=10)

        # Bottone per tornare indietro
        tk.Button(self.window, text="Torna al Menu", command=self.chiudi_gioco).pack()

    def scommetti(self, numero):
        # Se abbiamo soldi, aggiungiamo 100€ alla puntata sul numero scelto
        if self.budget >= 100:
            self.budget -= 100
            self.puntate[numero] = self.puntate.get(numero, 0) + 100
            self.lbl_budget.config(text=f"Budget: €{self.budget}")
            print(f"Puntati 100€ sul numero {numero}")

    def avvia_gioco(self):
        # Controlla che non stia già girando e che ci siano puntate
        if not self.in_corso and self.puntate:
            self.in_corso = True
            self.muovi_pallina(100) # Inizia l'animazione con 100 scatti

    def muovi_pallina(self, passi):
        # Calcola la posizione della pallina lungo il cerchio
        rad = math.radians(self.angolo - 90)
        x, y = 200 + 150 * math.cos(rad), 200 + 150 * math.sin(rad)
        self.canvas.coords(self.pallina, x-5, y-5, x+5, y+5) # Sposta il cerchietto bianco
        
        if passi > 0:
            self.angolo += 20 # Velocità di rotazione
            # Richiama questa stessa funzione dopo 30 millisecondi (crea l'animazione)
            self.window.after(30, lambda: self.muovi_pallina(passi - 1))
        else:
            self.calcola_vincita()

    def calcola_vincita(self):
        # Trova il numero su cui si è fermata la pallina
        indice = round((self.angolo % 360) / (360/37)) % 37
        risultato = self.numeri[indice]
        
        # Verifica se l'utente ha vinto (moltiplicatore x36)
        vincita = self.puntate.get(risultato, 0) * 36
        self.budget += vincita
        
        messagebox.showinfo("Risultato", f"È uscito il numero: {risultato}\nHai vinto: €{vincita}")
        
        # Reset per il prossimo giro
        self.lbl_budget.config(text=f"Budget: €{self.budget}")
        self.puntate = {}
        self.in_corso = False

    def chiudi_gioco(self):
        # Prima di distruggere la finestra, invia il budget aggiornato al menu principale
        self.callback(self.budget)
        self.window.destroy()

# --- CLASSE MENU PRINCIPALE (LOBBY) ---
class MenuPrincipale:
    def __init__(self, root):
        self.root = root
        self.root.title("3M Casino - Lobby")
        self.root.geometry("400x300")
        
        self.wallet = 5000 # Saldo totale del giocatore
        
        # Etichetta saldo
        self.lbl_wallet = tk.Label(root, text=f"Saldo Totale: €{self.wallet}", font=("Arial", 14))
        self.lbl_wallet.pack(pady=20)
        
        # Bottone per aprire la roulette
        tk.Button(root, text="Gioca alla Roulette", font=("Arial", 12), width=20, command=self.apri_roulette).pack(pady=10)
        
        # Bottone per uscire
        tk.Button(root, text="Esci dal Casino", command=root.quit).pack(pady=10)

    def apri_roulette(self):
        # Crea il gioco passandogli il wallet attuale e la funzione 'ricevi_budget'
        Roulette(self.root, self.wallet, self.ricevi_budget)

    def ricevi_budget(self, budget_finale):
        # Questa funzione viene chiamata dalla Roulette quando si chiude
        self.wallet = budget_finale
        self.lbl_wallet.config(text=f"Saldo Totale: €{self.wallet}")

# --- AVVIO DEL PROGRAMMA ---
if __name__ == "__main__":
    finestra_base = tk.Tk() # Crea la finestra radice
    app = MenuPrincipale(finestra_base) # Avvia il menu
    finestra_base.mainloop() # Mantiene la finestra aperta
