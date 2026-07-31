import random

class Carta:
    def __init__(self, figura, seme, nome):
        self.figura = figura
        self.seme = seme
        self.nome = nome
        self.valore = 0

class Mazzo:
    mazzo = []

    @classmethod
    def shuffle(cls):
        random.shuffle(cls.mazzo)

    @classmethod
    def crea_mazzo(cls):
        semi = ("♥", "♦", "♣", "♠")
        figure = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
        for seme in semi:
            for figura in figure:
                nome = f"{figura} di {seme}"
                cls.mazzo.append(Carta(figura, seme, nome))

    @classmethod
    def distribuire_carte(cls, num):
        for i in range(num):
            carta = cls.mazzo.pop(0)
            Giocatore.mano.append(carta)

class Giocatore:
    mano = []
    grafica_mano = []
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
        for carta in cls.mano:
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

class Banco(Giocatore):
    pass

alex = Giocatore("Alex", scommessa = -100)
Mazzo.crea_mazzo()
Mazzo.shuffle()
Mazzo.distribuire_carte(6)
alex.mostra_mano()