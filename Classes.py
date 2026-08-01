import random
# import time

class Carta:
    def __init__(self, figura, seme, nome, valore):
        self.figura = figura
        self.seme = seme
        self.nome = nome
        self.valore = valore

    def asso(self, carta):
        if carta in Banco.mano:
            if Banco.punti + 11 > 21:
                self.valore = 1
            else:
                self.valore = 11
        else:
            if Giocatore.punti + 11 > 21:
                self.valore = 1
            else:
                value = int(input("Inserisci un valore per l'asso (1/11): "))
                while True:
                    try:
                        value = int(value)
                        match value:
                            case 1 | 11:
                                self.valore = value
                                break
                            case _:
                                value = int(input("Devi inserire uno tra i due numeri (1/11): "))
                    except ValueError:
                        value = input("Devi inserire un numero: ")

class Mazzo:
    mazzo = []

    @classmethod
    def shuffle(cls):
        random.shuffle(cls.mazzo)

    @classmethod
    def crea_mazzo(cls):
        semi = ("♥", "♦", "♣", "♠")
        figure = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
        Banco.mano.append(Carta(0, 0, 0, 0))
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
                cls.mazzo.append(Carta(figura, seme, nome, valore))

class Giocatore:
    mano = []
    grafica_mano = []
    punti = 0
    def __init__(self, nome, scommessa):
        self.nome = nome
        self.scommessa = scommessa

    @property
    def scommessa(self):
        return self.scommessa

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

    @classmethod
    def mostra_mano(cls):
        cls.grafica_mano = []
        for carta in cls.mano:
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
            cls.grafica_mano.append(grafica)

        horiz = 0
        for riga in range(7):
            for sezione in cls.grafica_mano:
                print(sezione[horiz], end=" ")
            horiz += 1
            print()

    @classmethod
    def calcola_punteggio(cls):
        punteggio = 0
        for carta in cls.mano:
            if carta.valore == (1, 11):
                carta.asso(carta)
                punteggio += carta.valore
            else:
                punteggio += carta.valore
        cls.punti += (punteggio - cls.punti)

    @classmethod
    def distribuire_carte(cls, num):
        if num == 2:
            if cls.mano[0].valore == 0:
                cls.mano.append(Mazzo.mazzo.pop(0))
            else:
                for _ in range(num):
                    cls.mano.append(Mazzo.mazzo.pop(0))
        elif num == 3 and cls.mano[0].valore == 0:
            del cls.mano[0]
            cls.mano.insert(0, Mazzo.mazzo.pop(0))
        elif (num - 2) == len(cls.mano):
            for _ in range(num - len(cls.mano) - 1):
                cls.mano.append(Mazzo.mazzo.pop(0))

    def risultati(self):
        if Giocatore.punti == 21 and len(Giocatore.mano) == 2 and Banco.punti != 21:
            self.scommessa = (self.scommessa * 5) / 2
            print(f"Blackjack! Riscuoti {self.scommessa} euro!!")
        elif Giocatore.punti == Banco.punti or (Giocatore.punti > 21 and Banco.punti > 21):
            print(f"La tua scommessa rimane intoccata, ed ammonta a {self.scommessa} euro!!")
        elif 21 >= Giocatore.punti > Banco.punti or Banco.punti > 21 > Giocatore.punti:
            self.scommessa *= 2
            print(f"Hai vinto!! Riscuoti {self.scommessa} euro!!")
        else:
            print(f"Hai perso {self.scommessa} euro!!")
            self.scommessa = 0

    def giocare_ancora(self):
        decisione = input("Vuoi continuare (Sì/No)? ").capitalize()
        while decisione != "Sì" and decisione != "Si" and decisione != "No":
            decisione = input("Devi scegliere tra <Sì> e <No>: ").capitalize()
        if decisione == "No":
            Gioco.is_running = False
        old_bet = self.scommessa

        nuova_scommessa = input("Inserisci la nuova scommessa: ")
        while self.scommessa == 0:
            try:
                nuova_scommessa = int(nuova_scommessa)
                if nuova_scommessa <= 0:
                    nuova_scommessa = int(input("Devi inserire un numero maggiore di 0: "))
                else:
                    self.scommessa = nuova_scommessa
            except ValueError:
                nuova_scommessa = input("Devi inserire un numero: ")

        if old_bet > 0:
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
                            self.scommessa += aggiunta_scommessa
                            break
                    except ValueError:
                        aggiunta_scommessa = input("Devi inserire un numero: ")

class Banco(Giocatore):
    mano = []
    grafica_mano = []
    punti = 0

    @classmethod
    def mostra_mano(cls):
        super().mostra_mano()

    @classmethod
    def calcola_punteggio(cls):
        super().calcola_punteggio()

    @classmethod
    def distribuire_carte(cls, num):
        super().distribuire_carte(num)

    @classmethod
    def prendere(cls):
        turn = 3
        while cls.punti < 17:
            cls.distribuire_carte(turn)
            cls.mostra_mano()
            cls.calcola_punteggio()
            print(cls.punti)
            turn += 1

class Gioco:
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