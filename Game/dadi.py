import random
import tkinter as tk
from tkinter import messagebox


class DadiGame:
    """Minigioco dei Dadi con interfaccia grafica"""

    def __init__(self, root, saldo_attuale, aggiorna_saldo_callback):
        self.main_root = root
        self.root = tk.Toplevel(root)
        self.saldo_attuale = saldo_attuale
        self.aggiorna_saldo_callback = aggiorna_saldo_callback
        
        self.root.title("Lancio dei Dadi 🎲")
        self.root.geometry("500x400")
        self.root.configure(bg="#1a1a1a")
        
        # Intercettiamo la "X" della finestra
        self.root.protocol("WM_DELETE_WINDOW", self.chiudi_gioco)
        
        # Variabili di gioco
        self.puntata_attuale = 0
        self.costo_gioco = 10
        
        self.crea_interfaccia()
        self.mostra_schermata_puntata()
    
    def crea_interfaccia(self):
        """Crea gli elementi dell'interfaccia"""
        # Titolo
        titolo = tk.Label(
            self.root,
            text="🎲 LANCIO DEI DADI 🎲",
            font=("Helvetica", 22, "bold"),
            bg="#1a1a1a",
            fg="#ffd700"
        )
        titolo.pack(pady=20)
        
        # Mostra il saldo
        self.lbl_saldo = tk.Label(
            self.root,
            text=f"Saldo: {self.saldo_attuale}€",
            font=("Helvetica", 14, "bold"),
            bg="#1a1a1a",
            fg="#ffffff"
        )
        self.lbl_saldo.pack(pady=5)
        
        # Costo del gioco
        costo_lbl = tk.Label(
            self.root,
            text=f"Costo per giocare: {self.costo_gioco}€",
            font=("Helvetica", 11),
            bg="#1a1a1a",
            fg="#b3b3b3"
        )
        costo_lbl.pack(pady=5)
        
        # Linea separatrice
        separatore = tk.Frame(self.root, bg="#404040", height=2)
        separatore.pack(fill="x", padx=20, pady=10)
        
        # Frame per i dadi
        self.frame_dadi = tk.Frame(self.root, bg="#1a1a1a")
        self.frame_dadi.pack(pady=20)
        
        # Primo dado
        self.frame_dado1 = tk.Frame(self.frame_dadi, bg="#262626", width=60, height=60)
        self.frame_dado1.pack(side="left", padx=20)
        
        self.lbl_dado1 = tk.Label(
            self.frame_dado1,
            text="?",
            font=("Helvetica", 40, "bold"),
            bg="#262626",
            fg="#ffd700",
            width=3,
            height=2
        )
        self.lbl_dado1.pack()
        
        # Secondo dado
        self.frame_dado2 = tk.Frame(self.frame_dadi, bg="#262626", width=60, height=60)
        self.frame_dado2.pack(side="left", padx=20)
        
        self.lbl_dado2 = tk.Label(
            self.frame_dado2,
            text="?",
            font=("Helvetica", 40, "bold"),
            bg="#262626",
            fg="#ffd700",
            width=3,
            height=2
        )
        self.lbl_dado2.pack()
        
        # Somma totale
        self.lbl_somma = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 14, "bold"),
            bg="#1a1a1a",
            fg="#ffffff"
        )
        self.lbl_somma.pack(pady=10)
        
        # Label per il risultato
        self.lbl_risultato = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 12),
            bg="#1a1a1a",
            fg="#ffffff",
            wraplength=400
        )
        self.lbl_risultato.pack(pady=10)
        
        # Bottone per giocare
        self.btn_gioca = tk.Button(
            self.root,
            text="Lancia i Dadi!",
            command=self.lancia_dadi,
            font=("Helvetica", 12, "bold"),
            bg="#ffd700",
            fg="#000000",
            activebackground="#e6c200",
            bd=0,
            cursor="hand2"
        )
        self.btn_gioca.pack(pady=15, ipady=8, padx=40, fill="x")
        
        # Bottone per tornare al menu
        self.btn_menu = tk.Button(
            self.root,
            text="Torna al Menu Principale",
            command=self.chiudi_gioco,
            font=("Helvetica", 10, "bold"),
            bg="#8b0000",
            fg="#ffffff",
            activebackground="#a30000",
            bd=0,
            cursor="hand2"
        )
        self.btn_menu.pack(pady=5, ipady=5, padx=40, fill="x")
    
    def mostra_schermata_puntata(self):
        """Mostra la schermata di puntata"""
        # Resetta i dadi
        self.lbl_dado1.config(text="?")
        self.lbl_dado2.config(text="?")
        self.lbl_somma.config(text="")
        self.lbl_risultato.config(text="Clicca il bottone per iniziare!")
        self.btn_gioca.config(state="normal")
    
    def lancia_dadi(self):
        """Logica principale del gioco"""
        # Controlla saldo
        if self.saldo_attuale < self.costo_gioco:
            messagebox.showerror(
                "Errore",
                f"Saldo insufficiente!\nHai: {self.saldo_attuale}€\nCosto: {self.costo_gioco}€",
                parent=self.root
            )
            return
        
        # Sottrae il costo
        self.saldo_attuale -= self.costo_gioco
        self.lbl_saldo.config(text=f"Saldo: {self.saldo_attuale}€")
        
        # Genera i due dadi
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        somma = dado1 + dado2
        
        # Mostra i dadi animati
        self.lbl_dado1.config(text=str(dado1))
        self.lbl_dado2.config(text=str(dado2))
        self.lbl_somma.config(text=f"Somma: {somma}")
        
        # Logica vincita
        if somma > 7:
            premio = 25
            self.saldo_attuale += premio
            variazione = premio - self.costo_gioco  # +15€ guadagno netto
            risultato = f"✅ VITTORIA!\nHai lanciato {somma} (> 7)\nVinci: {premio}€\nGuadagno netto: +{variazione}€"
            colore = "#2ecc71"  # Verde
        else:
            variazione = -self.costo_gioco  # -10€
            risultato = f"❌ SCONFITTA!\nHai lanciato {somma} (≤ 7)\nPerdita: -{self.costo_gioco}€"
            colore = "#e74c3c"  # Rosso
        
        self.lbl_risultato.config(text=risultato, fg=colore)
        self.lbl_saldo.config(text=f"Saldo: {self.saldo_attuale}€")
        
        # Salva il risultato nel database (verrà gestito da main.py)
        self.puntata_attuale = {
            "gioco": "Dadi",
            "variazione": variazione,
            "saldo_risultante": self.saldo_attuale
        }
        
        # Chiede se rigiocare
        def rigiocare():
            self.mostra_schermata_puntata()
        
        def tornare_menu():
            self.chiudi_gioco()
        
        # Frame per i bottoni di scelta
        frame_scelta = tk.Frame(self.root, bg="#1a1a1a")
        frame_scelta.pack(pady=10)
        
        # Ricrea i bottoni
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame) and widget != self.frame_dadi:
                if widget != frame_scelta:
                    continue
        
        # Bottone ancora il gioco per semplificare
        self.btn_gioca.config(state="normal")
        self.btn_menu.config(state="normal")
    
    def chiudi_gioco(self):
        """Chiude la finestra e aggiorna il saldo nel main"""
        self.root.destroy()
        self.aggiorna_saldo_callback(self.saldo_attuale)


def start_game(root, saldo_attuale, aggiorna_saldo_callback):
    """Avvia una nuova partita di Dadi"""
    DadiGame(root, saldo_attuale, aggiorna_saldo_callback)
