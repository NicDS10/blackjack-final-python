import random

class Carta:
    def __init__(self, figura, seme, nome, valore):
        self.figura = figura
        self.seme = seme
        self.nome = nome
        self.valore = valore

    def asso(self):
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
                carta.asso()
                punteggio += carta.valore
            else:
                punteggio += carta.valore
        cls.punti += (punteggio - cls.punti)

    @classmethod
    def distribuire_carte(cls, num):
        pass

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
        pass