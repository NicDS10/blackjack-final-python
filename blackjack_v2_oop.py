from Classes import *
# import time

def main():
    nome = input("Inserisci il tuo nome: ")
    scommessa = input("Inserisci la somma che vuoi scommettere: ")
    player = Giocatore(nome, scommessa)
    print()
    Game.presentazione()
    banco = Banco()
    carte = Mazzo()
    while Game.is_running:
        carte.mazzo = []
        player.mano, player.grafica_mano, player.punti = [], [], 0
        banco.mano, banco.grafica_mano, banco.punti = [], [], 0
        carte.crea_mazzo(banco, player)
        player.distribuire_carte(2, carte)
        player.mostra_mano()
        player.calcola_punteggio(banco)
        banco.distribuire_carte(2, carte)
        banco.mostra_mano()
        banco.calcola_punteggio(banco)
        Game.turno_giocatore()
        player.continuare(carte, banco)
        Game.turno_banco()
        banco.prendere(carte, banco)
        player.risultati(banco)
        player.giocare_ancora()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n Il programma è stato interrotto dall'utente.")
    except ValueError:
        print("\n Una conversiona è fallita, \n l'utente è pregato di inserire numeri interi quando richiesto.")