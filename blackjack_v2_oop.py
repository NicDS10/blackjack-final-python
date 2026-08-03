from Classes import Giocatore, Banco, Mazzo, Game

def main():
    nome = input("Inserisci il tuo nome: ")
    scommessa = input("Inserisci la somma che vuoi scommettere: ")
    player = Giocatore(nome, scommessa)
    print()
    time.sleep(1)
    Game.presentazione()
    time.sleep(1)
    banco = Banco()
    carte = Mazzo()
    while Game.is_running:
        carte.mazzo = []
        player.mano, player.grafica_mano, player.punti = [], [], 0
        banco.mano, banco.grafica_mano, banco.punti, banco.turni = [], [], 0, 0
        carte.crea_mazzo(banco, player)
        player.distribuire_carte(2, carte)
        print()
        player.mostra_mano()
        player.calcola_punteggio(banco)
        banco.distribuire_carte(2, carte)
        time.sleep(1.6)
        print()
        banco.mostra_mano()
        banco.calcola_punteggio(banco)
        time.sleep(1.3)
        if player.punti < 21:
            print()
            Game.turno_giocatore()
            time.sleep(1.3)
        print()
        player.continuare(carte, banco)
        print()
        time.sleep(1.3)
        Game.turno_banco()
        print()
        banco.prendere(carte, banco)
        print()
        player.risultati(banco)
        print()
        player.giocare_ancora()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n Il programma è stato interrotto dall'utente.")
    except ValueError:
        print("\n Una conversiona è fallita, \n l'utente è pregato di inserire numeri interi quando richiesto.")