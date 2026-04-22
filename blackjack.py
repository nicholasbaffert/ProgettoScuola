import random

semi_carte = {'Cuori': '♥️', 'Quadri': '♦️', 'Fiori': '♣️', 'Picche': '♠️'} # Definizione dei semi delle carte
lista_carte = ['Asso', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Fante', 'Regina', 'Re'] # Definizione dei valori delle carte
mazzo = [] # Inizializzazione del mazzo
for seme in semi_carte.keys(): # Cicla su ogni seme
    for carta in lista_carte: # Cicla su ogni valore
        mazzo.append((carta, seme)) # Definizione del mazzo completa da 52 carte

def valore_carta(carta_tupla): # Definizione delle carte delle figure
    nome_carta = carta_tupla[0]
    if nome_carta in ['Fante', 'Regina', 'Re']: 
        return 10
    elif nome_carta == 'Asso':
        return 11
    else:
        return int(nome_carta)

def mostra_mano(nome, carte, punteggio, nascondi_seconda=False):
    print(f"\n--- {nome.upper()} ---")
    
    if nascondi_seconda:
        valore, seme = carte[0]
        print(f"🎴 Carte: {valore} di {semi_carte[seme]} , [CARTA COPERTA]")
        print(f"🔢 Punteggio visibile: {valore_carta(carte[0])}")
    else:
        stringa = []
        for valore, simbolo in carte:
            stringa.append(f"{valore} di {semi_carte[simbolo]}")
        
        print(f"🎴 Carte: {' , '.join(stringa)}")
        print(f"🔢 Punteggio totale: {punteggio}")


random.shuffle(mazzo) # Mischia il mazzo
carte_giocatore = [mazzo.pop(), mazzo.pop()] # Distribuisce le carte al giocatore
carte_banco = [mazzo.pop(), mazzo.pop()] # Distribuisce le carte al banco

while True:
    punteggio_giocatore = 0
    punteggio_banco = 0

    for carta in carte_giocatore:
        valore = valore_carta(carta)
        punteggio_giocatore = punteggio_giocatore + valore
    
    for carta in carte_banco:
        valore = valore_carta(carta)
        punteggio_banco = punteggio_banco + valore
    
    mostra_mano("Giocatore", carte_giocatore, punteggio_giocatore)
    mostra_mano("Banco", carte_banco, punteggio_banco, nascondi_seconda=True)

    if punteggio_giocatore > 21:
        print("Il Banco vince")
        break

    scelta = input("Cosa vuoi fare?\n'carta' per chiedere un\'altra carta, 'stai' per fermarti: ")
    scelta = scelta.lower()
    if scelta == "carta":
        nuova_carta = mazzo.pop()
        carte_giocatore.append(nuova_carta)
    elif scelta == "stai":
        break
    else:
        print("Scelta non valida")
        continue

if punteggio_giocatore <= 21:
    while punteggio_banco < 17:
        nuova_carta = mazzo.pop()
        carte_banco.append(nuova_carta)
        punteggio_banco = punteggio_banco + valore_carta(nuova_carta)

print("\n" + "="*30)
print("RISULTATO FINALE")
print("="*30)
mostra_mano("Giocatore", carte_giocatore, punteggio_giocatore)
mostra_mano("Banco", carte_banco, punteggio_banco)

if punteggio_banco > 21:
        print("\n🏆 Il Giocatore vince!  (Il Banco ha sballato)")
elif punteggio_giocatore > punteggio_banco:
        print("\n🏆 Il Giocatore vince!")
elif punteggio_banco > punteggio_giocatore:
        print("\n📉 Il Banco vince")
else:
        print("\n🤝 È un pareggio!")