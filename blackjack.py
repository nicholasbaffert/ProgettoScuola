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


def calcola_punteggio(mano):
    punteggio = 0
    for carta in mano:
        punteggio = punteggio + valore_carta(carta)
    num_assi = 0
    for carta in mano:
        if carta[0] == 'Asso':
            num_assi = num_assi + 1
    while punteggio > 21 and num_assi > 0:
        punteggio = punteggio - 10
        num_assi = num_assi - 1
    return punteggio


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

punteggio_giocatore = calcola_punteggio(carte_giocatore)
punteggio_banco = calcola_punteggio(carte_banco)

BLACKJACK_GIOCATORE = (punteggio_giocatore == 21)
BLACKJACK_BANCO = (punteggio_banco == 21)

if not BLACKJACK_GIOCATORE and not BLACKJACK_BANCO:
    while True:
        punteggio_giocatore = calcola_punteggio(carte_giocatore)
        mostra_mano("Giocatore", carte_giocatore, punteggio_giocatore)
        mostra_mano("Banco", carte_banco, punteggio_banco, nascondi_seconda=True)

        if punteggio_giocatore >= 21:
            break

        scelta = input("Cosa vuoi fare?\n'hit' per chiedere un\'altra carta, 'stand' per fermarti: ")
        scelta = scelta.lower()
        
        if scelta == "hit":
            nuova_carta = mazzo.pop()
            carte_giocatore.append(nuova_carta)
        elif scelta == "stand":
            break
        else:
            print("Scelta non valida")
            continue

if punteggio_giocatore <= 21 and not BLACKJACK_GIOCATORE:
    while punteggio_banco < 17:
        nuova_carta = mazzo.pop()
        carte_banco.append(nuova_carta)
        punteggio_banco = calcola_punteggio(carte_banco)


print("\n" + "="*30)
print("RISULTATO FINALE")
print("="*30)
mostra_mano("Giocatore", carte_giocatore, punteggio_giocatore)
mostra_mano("Banco", carte_banco, punteggio_banco)


if BLACKJACK_GIOCATORE and BLACKJACK_BANCO:
    print("\n🤝 Entrambi Blackjack! Pareggio.")
elif BLACKJACK_GIOCATORE:
    print("\n🏆 BLACKJACK! Hai vinto subito!")
elif BLACKJACK_BANCO:
    print("\n📉 Il Banco ha fatto Blackjack. Hai perso.")
elif punteggio_giocatore > 21:
    print("\n📉 Hai sballato! Il Banco vince")
elif punteggio_banco > 21:
    print("\n🏆 Il Giocatore vince! (Il Banco ha sballato)")
elif punteggio_giocatore > punteggio_banco:
    print("\n🏆 Il Giocatore vince!")
elif punteggio_banco > punteggio_giocatore:
    print("\n📉 Il Banco vince")
else:
    print("\n🤝 È un pareggio!")