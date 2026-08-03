import random
import time

class Carta:
    def __init__(self, figura, seme, nome, valore):
        self.figura = figura
        self.seme = seme
        self.nome = nome
        self.valore = valore

class Mazzo:
    def __init__(self):
        self.mazzo = []

    def shuffle(self):
        random.shuffle(self.mazzo)

    def crea_mazzo(self, banco, player):
        semi = ("♥", "♦", "♣", "♠")
        figure = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
        banco.mano.append(Carta(0, 0, 0, 0))
        for seme in semi:
            for figura in figure:
                nome = f"{figura} di {seme}"
                match figura:
                    case "J" | "Q" | "K":
                        valore = 10
                    case "A":
                        valore = (1, 11)
                    case _:
                        valore = int(figura)
                self.mazzo.append(Carta(figura, seme, nome, valore))
        self.shuffle()
        player.mano.append(self.mazzo.pop(0))

class Giocatore:
    def __init__(self, nome, scommessa):
        self.nome = nome
        self.scommessa = scommessa
        self.mano = []
        self.grafica_mano = []
        self.punti = 0

    @property
    def scommessa(self):
        return self._scommessa

    @scommessa.setter
    def scommessa(self, importo):
        while True:
            try:
                importo = int(importo)
                if importo > 0:
                    self._scommessa = importo
                    break
                else:
                    importo = int(input("Devi inserire un numero positivo: "))
            except ValueError:
                importo = input("Devi inserire un numero: ")

    def mostra_mano(self):
        self.grafica_mano = []
        for carta in self.mano:
            if carta.valore == 0:
                grafica = ("?????????????",
                           "?  ?        ?",
                           "?           ?",
                           "?     ?     ?",
                           "?           ?",
                           "?        ?  ?",
                           "?????????????")
            else:
                grafica = (r" /---------\ ",
                           f"| {carta.figura:>2}        |",
                           "|           |",
                           f"|     {carta.seme}     |",
                           "|           |",
                           f"|        {carta.figura:>2} |",
                           r" \---------/ ")
            self.grafica_mano.append(grafica)

        horiz = 0
        for riga in range(7):
            for sezione in self.grafica_mano:
                print(sezione[horiz], end=" ")
            horiz += 1
            print()

    def calcola_punteggio(self, banco):
        punteggio = 0
        for carta in self.mano:
            if carta.valore == (1, 11):
                self.asso(carta, banco)
                punteggio += carta.valore
            else:
                punteggio += carta.valore
        self.punti += (punteggio - self.punti)
        if self.mano[0].valore == 0 or banco.turni > 1:
            print(f"Il punteggio del banco è {self.punti}")
            banco.turni += 1
            if self.punti > 21:
                print("Il banco ha sballato!")
        else:
            print(f"Il tuo punteggio è {self.punti}")
            if self.punti > 21:
                print("Hai sballato!")
            if punteggio == 21 and len(self.mano) == 2 and self.mano[-1].valore == 10:
                print("Hai fatto Blackjack!")

    def distribuire_carte(self, num, carte):
        if num == 2:
            if self.mano[0].valore == 0:
                self.mano.append(carte.mazzo.pop(0))
            else:
                self.mano.append(carte.mazzo.pop(0))
        elif num == 3 and self.mano[0].valore == 0:
            del self.mano[0]
            self.mano.insert(0, carte.mazzo.pop(0))
        elif (num - 2) == len(self.mano):
            for _ in range(num - len(self.mano) - 1):
                self.mano.append(carte.mazzo.pop(0))

    def risultati(self, banco):
        if self.punti == 21 and len(self.mano) == 2 and banco.punti != 21:
            self._scommessa = (self._scommessa * 5) / 2
            print(f"Blackjack! Riscuoti {self._scommessa} euro!!")
        elif self.punti == banco.punti or (self.punti > 21 and banco.punti > 21):
            print(f"La tua scommessa rimane intoccata, ed ammonta a {self._scommessa} euro!!")
        elif 21 >= self.punti > banco.punti or banco.punti > 21 > self.punti:
            self._scommessa *= 2
            print(f"Hai vinto!! Riscuoti {self._scommessa} euro!!")
        elif self.punti == 21 and len(self.mano) > 2 and banco.punti == 21 and len(banco.mano) == 2:
            print(f"Hai totalizzato {self.punti}, ma il banco ha fatto Blackjack! Hai perso {self.scommessa} euro!!")
            self._scommessa = 0
        else:
            print(f"Hai perso {self._scommessa} euro!!")
            self._scommessa = 0

    def giocare_ancora(self):
        decisione = input("Vuoi continuare (Sì/No)? ").capitalize()
        while decisione != "Sì" and decisione != "Si" and decisione != "No":
            decisione = input("Devi scegliere tra <Sì> e <No>: ").capitalize()
        if decisione == "No":
            Game.is_running = False
        old_bet = self._scommessa

        if self._scommessa == 0 and Game.is_running:
            nuova_scommessa = input("Inserisci la nuova scommessa: ")
            while True:
                try:
                    nuova_scommessa = int(nuova_scommessa)
                    if nuova_scommessa <= 0:
                        nuova_scommessa = int(input("Devi inserire un numero maggiore di 0: "))
                    else:
                        self._scommessa = nuova_scommessa
                        break
                except ValueError:
                    nuova_scommessa = input("Devi inserire un numero: ")

        if old_bet > 0 and Game.is_running:
            decision = input("Vuoi aggiungere una scommessa (Sì/No)? ").capitalize()
            while decision != "Sì" and decision != "Si" and decision != "No":
                decision = input("Devi scegliere tra <Sì> e <No>: ").capitalize()
            if decision == "Sì" or decision == "Si":
                aggiunta_scommessa = input("Inserisci la somma da aggiungere alla scommessa: ")
                while True:
                    try:
                        aggiunta_scommessa = int(aggiunta_scommessa)
                        if aggiunta_scommessa <= 0:
                            aggiunta_scommessa = int(input("Devi inserire un numero maggiore di 0: "))
                        else:
                            self._scommessa += aggiunta_scommessa
                            break
                    except ValueError:
                        aggiunta_scommessa = input("Devi inserire un numero: ")

    def asso(self, carta, banco):
        if carta in banco.mano:
            if banco.punti + 11 > 21:
                carta.valore = 1
            else:
                carta.valore = 11
        else:
            if self.punti + 11 > 21:
                carta.valore = 1
            elif self.punti + 11 == 21:
                carta.valore = 11
                print(f"Hai fatto Blackjack {self.nome}!")
            else:
                value = int(input("Inserisci un valore per l'asso (1/11): "))
                while True:
                    try:
                        value = int(value)
                        match value:
                            case 1 | 11:
                                carta.valore = value
                                break
                            case _:
                                value = int(input("Devi inserire uno tra i due numeri (1/11): "))
                    except ValueError:
                        value = input("Devi inserire un numero: ")

    def continuare(self, carte, banco):
        turno = 3
        dec = "Prendere"
        while self.punti < 21 and dec == "Prendere":
            print()
            self.distribuire_carte(turno, carte)
            self.mostra_mano()
            self.calcola_punteggio(banco)
            print()
            turno += 1
            if self.punti < 21:
                dec = input("Vuoi continuare (prendere/lasciare)? ").capitalize()
                while dec != "Prendere" and dec != "Lasciare":
                    dec= input("Devi scegliere tra <prendere> e <lasciare>: ").capitalize()
            else:
                break
            time.sleep(1)
        banco.turni += 1

class Banco(Giocatore):
    def __init__(self):
        super().__init__(nome = "", scommessa = 1)
        self.mano = []
        self.grafica_mano = []
        self.punti = 0
        self.turni = 0

    def prendere(self, carte, banco):
        turn = 3
        while self.punti < 17:
            self.distribuire_carte(turn, carte)
            self.mostra_mano()
            self.calcola_punteggio(banco)
            time.sleep(1)
            turn += 1
            print()

class Game:
    is_running = True

    @staticmethod
    def presentazione():
        print("----------------- Benvenuto su Blackjack!! -----------------")

    @staticmethod
    def turno_giocatore():
        print("----------------- È il tuo turno! -----------------")

    @staticmethod
    def turno_banco():
        print("----------------- È il turno del banco! -----------------")