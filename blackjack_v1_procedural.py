import time
import random

carte = {0 : ("?????????????",
              "?           ?",
              "?           ?",
              "?           ?",
              "?           ?",
              "?           ?",
              "?????????????",),
         11 : (r" /---------\ ",
               "| A         |",
               "|           |",
               "|     ♣     |",
               "|           |",
               "|         A |",
               r" \---------/ "),
         12 : (r" /---------\ ",
               "| A         |",
               "|           |",
               "|     ♠     |",
               "|           |",
               "|         A |",
               r" \---------/ "),
         13 : (r" /---------\ ",
               "| A         |",
               "|           |",
               "|     ♦     |",
               "|           |",
               "|         A |",
               r" \---------/ "),
         14 : (r" /---------\ ",
               "| A         |",
               "|           |",
               "|     ♥     |",
               "|           |",
               "|         A |",
               r" \---------/ "),
         21 : (r" /---------\ ",
               "| 2         |",
               "|           |",
               "|     ♣     |",
               "|           |",
               "|         2 |",
               r" \---------/ "),
         22 : (r" /---------\ ",
               "| 2         |",
               "|           |",
               "|     ♠     |",
               "|           |",
               "|         2 |",
               r" \---------/ "),
         23 : (r" /---------\ ",
               "| 2         |",
               "|           |",
               "|     ♦     |",
               "|           |",
               "|         2 |",
               r" \---------/ "),
         24 : (r" /---------\ ",
               "| 2         |",
               "|           |",
               "|     ♥     |",
               "|           |",
               "|         2 |",
               r" \---------/ "),
         31 : (r" /---------\ ",
               "| 3         |",
               "|           |",
               "|     ♣     |",
               "|           |",
               "|         3 |",
               r" \---------/ "),
         32 : (r" /---------\ ",
               "| 3         |",
               "|           |",
               "|     ♠     |",
               "|           |",
               "|         3 |",
               r" \---------/ "),
         33 : (r" /---------\ ",
               "| 3         |",
               "|           |",
               "|     ♦     |",
               "|           |",
               "|         3 |",
               r" \---------/ "),
         34 : (r" /---------\ ",
               "| 3         |",
               "|           |",
               "|     ♥     |",
               "|           |",
               "|         3 |",
               r" \---------/ "),
         41 : (r" /---------\ ",
               "| 4         |",
               "|           |",
               "|     ♣     |",
               "|           |",
               "|         4 |",
               r" \---------/ "),
         42 : (r" /---------\ ",
               "| 4         |",
               "|           |",
               "|     ♠     |",
               "|           |",
               "|         4 |",
               r" \---------/ "),
         43 : (r" /---------\ ",
               "| 4         |",
               "|           |",
               "|     ♦     |",
               "|           |",
               "|         4 |",
               r" \---------/ "),
         44 : (r" /---------\ ",
               "| 4         |",
               "|           |",
               "|     ♥     |",
               "|           |",
               "|         4 |",
               r" \---------/ "),
         51 : (r" /---------\ ",
               "| 5         |",
               "|           |",
               "|     ♣     |",
               "|           |",
               "|         5 |",
               r" \---------/ "),
         52 : (r" /---------\ ",
               "| 5         |",
               "|           |",
               "|     ♠     |",
               "|           |",
               "|         5 |",
               r" \---------/ "),
         53 : (r" /---------\ ",
               "| 5         |",
               "|           |",
               "|     ♦     |",
               "|           |",
               "|         5 |",
               r" \---------/ "),
         54 : (r" /---------\ ",
               "| 5         |",
               "|           |",
               "|     ♥     |",
               "|           |",
               "|         5 |",
               r" \---------/ "),
         61 : (r" /---------\ ",
               "| 6         |",
               "|           |",
               "|     ♣     |",
               "|           |",
               "|         6 |",
               r" \---------/ "),
         62 : (r" /---------\ ",
               "| 6         |",
               "|           |",
               "|     ♠     |",
               "|           |",
               "|         6 |",
               r" \---------/ "),
         63 : (r" /---------\ ",
               "| 6         |",
               "|           |",
               "|     ♦     |",
               "|           |",
               "|         6 |",
               r" \---------/ "),
         64 : (r" /---------\ ",
               "| 6         |",
               "|           |",
               "|     ♥     |",
               "|           |",
               "|         6 |",
               r" \---------/ "),
         71 : (r" /---------\ ",
               "| 7         |",
               "|           |",
               "|     ♣     |",
               "|           |",
               "|         7 |",
               r" \---------/ "),
         72 : (r" /---------\ ",
               "| 7         |",
               "|           |",
               "|     ♠     |",
               "|           |",
               "|         7 |",
               r" \---------/ "),
         73 : (r" /---------\ ",
               "| 7         |",
               "|           |",
               "|     ♦     |",
               "|           |",
               "|         7 |",
               r" \---------/ "),
         74 : (r" /---------\ ",
               "| 7         |",
               "|           |",
               "|     ♥     |",
               "|           |",
               "|         7 |",
               r" \---------/ "),
         81 : (r" /---------\ ",
               "| 8         |",
               "|           |",
               "|     ♣     |",
               "|           |",
               "|         8 |",
               r" \---------/ "),
         82 : (r" /---------\ ",
               "| 8         |",
               "|           |",
               "|     ♠     |",
               "|           |",
               "|         8 |",
               r" \---------/ "),
         83 : (r" /---------\ ",
               "| 8         |",
               "|           |",
               "|     ♦     |",
               "|           |",
               "|         8 |",
               r" \---------/ "),
         84 : (r" /---------\ ",
               "| 8         |",
               "|           |",
               "|     ♥     |",
               "|           |",
               "|         8 |",
               r" \---------/ "),
         91 : (r" /---------\ ",
               "| 9         |",
               "|           |",
               "|     ♣     |",
               "|           |",
               "|         9 |",
               r" \---------/ "),
         92 : (r" /---------\ ",
               "| 9         |",
               "|           |",
               "|     ♠     |",
               "|           |",
               "|         9 |",
               r" \---------/ "),
         93 : (r" /---------\ ",
               "| 9         |",
               "|           |",
               "|     ♦     |",
               "|           |",
               "|         9 |",
               r" \---------/ "),
         94 : (r" /---------\ ",
               "| 9         |",
               "|           |",
               "|     ♥     |",
               "|           |",
               "|         9 |",
               r" \---------/ "),
         101 : (r" /---------\ ",
                "| 10        |",
                "|           |",
                "|     ♣     |",
                "|           |",
                "|        10 |",
                r" \---------/ "),
         102 : (r" /---------\ ",
                "| 10        |",
                "|           |",
                "|     ♠     |",
                "|           |",
                "|        10 |",
                r" \---------/ "),
         103 : (r" /---------\ ",
                "| 10        |",
                "|           |",
                "|     ♦     |",
                "|           |",
                "|        10 |",
                r" \---------/ "),
         104 : (r" /---------\ ",
                "| 10        |",
                "|           |",
                "|     ♥     |",
                "|           |",
                "|        10 |",
                r" \---------/ "),
         111 : (r" /---------\ ",
                "| J         |",
                "|           |",
                "|     ♣     |",
                "|           |",
                "|         J |",
                r" \---------/ "),
         112 : (r" /---------\ ",
                "| J         |",
                "|           |",
                "|     ♠     |",
                "|           |",
                "|         J |",
                r" \---------/ "),
         113 : (r" /---------\ ",
                "| J         |",
                "|           |",
                "|     ♦     |",
                "|           |",
                "|         J |",
                r" \---------/ "),
         114 : (r" /---------\ ",
                "| J         |",
                "|           |",
                "|     ♥     |",
                "|           |",
                "|         J |",
                r" \---------/ "),
         121 : (r" /---------\ ",
                "| Q         |",
                "|           |",
                "|     ♣     |",
                "|           |",
                "|         Q |",
                r" \---------/ "),
         122 : (r" /---------\ ",
                "| Q         |",
                "|           |",
                "|     ♠     |",
                "|           |",
                "|         Q |",
                r" \---------/ "),
         123 : (r" /---------\ ",
                "| Q         |",
                "|           |",
                "|     ♦     |",
                "|           |",
                "|         Q |",
                r" \---------/ "),
         124 : (r" /---------\ ",
                "| Q         |",
                "|           |",
                "|     ♥     |",
                "|           |",
                "|         Q |",
                r" \---------/ "),
         131 : (r" /---------\ ",
                "| K         |",
                "|           |",
                "|     ♣     |",
                "|           |",
                "|         K |",
                r" \---------/ "),
         132 : (r" /---------\ ",
                "| K         |",
                "|           |",
                "|     ♠     |",
                "|           |",
                "|         K |",
                r" \---------/ "),
         133 : (r" /---------\ ",
                "| K         |",
                "|           |",
                "|     ♦     |",
                "|           |",
                "|         K |",
               r" \---------/ "),
         134 : (r" /---------\ ",
                "| K         |",
                "|           |",
                "|     ♥     |",
                "|           |",
                "|         K |",
               r" \---------/ "),
         }
def ripeti(x):
    cas = x - len(carte_ottenute)
    for i in range(cas):
        carte_ottenute.append(random.choice(chiavi_carte))
        while carte_ottenute[-1] == 0:
            carte_ottenute.remove(0)
            carte_ottenute.append(random.choice(chiavi_carte))
        chiavi_carte.remove(carte_ottenute[-1])
    num1 = 0
    punti = 0
    for riga in range(7):
        num = 0
        for sezione in range(x):
            print(carte.get(carte_ottenute[num])[num1], end= " ")
            num += 1
        print()
        num1 += 1
    if x == 2:
        for i in range(x):
            if carte_ottenute[i] > 100:
                punti += 10
            elif 10 < carte_ottenute[i] < 15:
                if punti + 11 > 21:
                    punti += 1
                elif punti + 11 == 21:
                    punti += 11
                else:
                    asso = input("Hai ottenuto un asso, lo vuoi far valere 1 o 11? ")
                    while not asso.isdigit():
                        asso = input("Devi inserire un numero: ")
                    asso = int(asso)
                    while not asso == 1 and not asso == 11:
                        asso = input("Inserisci 1 o 11: ")
                        while not asso.isdigit():
                            asso = input("Devi inserire un numero: ")
                        asso = int(asso)
                    if asso == 1:
                        punti += 1
                    else:
                        punti += 11
            else:
                punti += int(str(carte_ottenute[i])[0])
            puntig.append(punti)
    else:
        if carte_ottenute[-1] > 100:
            puntig[-1] += 10
        elif 10 < carte_ottenute[-1] < 15:
            if puntig[-1] + 11 > 21:
                puntig[-1] += 1
            else:
                asso = input("Hai ottenuto un asso, lo vuoi far valere 1 o 11? ")
                while not asso.isdigit():
                    asso = input("Devi inserire un numero: ")
                asso = int(asso)
                while not asso == 1 and not asso == 11:
                    asso = input("Inserisci 1 o 11: ")
                    while not asso.isdigit():
                        asso = input("Devi inserire un numero: ")
                    asso = int(asso)
                if asso == 1:
                    puntig[-1] += 1
                else:
                    puntig[-1] += 11
        else:
            puntig[-1] += int(str(carte_ottenute[-1])[0])
    if puntig[-1] > 21:
        print("Hai sballato!")
    elif puntig[-1] == 21 and x == 2:
        print("Hai fatto blackjack!!")
    else:
        print(f"Il tuo punteggio è {puntig[-1]}")

def ripeti_b(y):
    if y == 2:
        carte_banco.append(0)
        carte_banco.append(random.choice(chiavi_carte))
        while carte_banco[-1] == 0:
            carte_banco.remove(carte_banco[-1])
            carte_banco.append(random.choice(chiavi_carte))
        chiavi_carte.remove(carte_banco[-1])
    elif y == 3:
        carte_banco[0] = random.choice(chiavi_carte)
        while carte_banco[-1] == 0:
            carte_banco.remove(carte_banco[-1])
            carte_banco.append(random.choice(chiavi_carte))
        chiavi_carte.remove(carte_banco[0])
    else:
        carte_banco.append(random.choice(chiavi_carte))
        while carte_banco[-1] == 0:
            carte_banco.remove(carte_banco[-1])
            carte_banco.append(random.choice(chiavi_carte))
        chiavi_carte.remove(carte_banco[-1])
    num1 = 0
    punti = 0
    for riga in range(7):
        num = 0
        for sezione in range(y if y == 2 else y - 1):
            print(carte.get(carte_banco[num])[num1], end=" ")
            num += 1
        print()
        num1 += 1
    for i in range(y if y == 2 else y - 1):
        if carte_banco[i] > 100:
            punti += 10
        elif 10 < carte_banco[i] < 15:
            if punti + 11 > 21:
                punti += 1
            else:
                punti += 11
        else:
            punti += int(str(carte_banco[i])[0])
    if punti > 21:
        print("Il banco ha sballato!")
    elif punti == 21 and y == 3:
        print("Il banco ha fatto blackhack!!")
    elif 16 < punti < 22:
        print(f"Il banco ha totalizzato {punti} punti!")
    else:
        print(f"Per ora il punteggio del banco è {punti}")
    puntib.append(punti)

print("----------------- Benvenuto su Blackjack!! -----------------")
time.sleep(1)
print()
scommessa = input("Quanti euro vuoi scommettere? ")
while not scommessa.isdigit():
    scommessa = input("Devi inserire un numero: ")
scommessa = int(scommessa)
running = True
while running:
    carte_ottenute = []
    carte_banco = []
    puntig = []
    puntib = []
    chiavi_carte = list(carte.keys())
    carte_ricevute = 2
    c = 2
    time.sleep(0.5)
    print()
    print("Il banco sta distribuendo le carte...")
    time.sleep(2.5)
    print()
    print("Le tue carte sono: ")
    time.sleep(0.3)
    ripeti(carte_ricevute)
    time.sleep(2)
    print()
    print("Le carte del banco sono: ")
    ripeti_b(c)
    print()
    time.sleep(1)
    if  puntig[-1] != 21:
        print("----------------- È il tuo turno! -----------------")
    time.sleep(1)
    decisione = 0
    while puntig[-1] < 21:
        print()
        decisione = input("Vuoi prendere o lasciare (p/l)? ").capitalize()
        while decisione != "L" and decisione != "P":
            decisione = input("Devi scegliere tra le due lettere (p/l): ").capitalize()
        if not puntig[-1] < 21 or not decisione == "P":
            break
        print()
        carte_ricevute += 1
        ripeti(carte_ricevute)
    p_finale = puntig[-1]
    time.sleep(1.5)
    print()
    print("----------------- È il turno del banco! -----------------")
    time.sleep(1.5)
    while puntib[-1] < 17:
        print()
        print("Il banco prende!")
        c += 1
        ripeti_b(c)
        time.sleep(2.5)
    print()
    p_banco = puntib[-1]
    if p_finale == p_banco or (p_finale > 21 and p_banco > 21):
        print(f"La tua scommessa rimane intoccata, ed ammonta a {scommessa} euro!!")
    elif decisione == 0:
        scommessa = (scommessa * 5) / 2
        print(f"Riscuoti {scommessa} euro!!")
    elif 22 > p_finale > p_banco or p_banco >= 22 > p_finale:
        scommessa = scommessa * 2
        print(f"Hai vinto!! Riscuoti {scommessa} euro!!")
    else:
        print(f"Hai perso {scommessa} euro!!")
        scommessa = 0
    print()
    time.sleep(1.5)
    cont = input("Vuoi continuare (Sì/No)? ").capitalize()
    while cont != "Sì" and cont != "Si" and cont != "No":
        cont = input("Devi scegliere tra <Sì> e <No>: ").capitalize()
    if cont == "No":
        break
    p = scommessa
    while scommessa < 1:
        n_scommessa = input("Inserisci la nuova scommessa (un numero): ")
        while not n_scommessa.isdigit():
            n_scommessa = input("Devi inserire un numero: ")
        scommessa = int(n_scommessa)
    if p > 0:
        dec = input("Vuoi aggiungere una scommessa (Sì/No)? ").capitalize()
        while dec != "Sì" and dec != "Si" and dec != "No":
            dec = input("Devi scegliere tra <Sì> e <No>: ").capitalize()
        if dec == "Sì" or dec == "Si":
            m_scommessa = input("Inserisci gli euro da aggiungere alla scommessa (un numero): ")
            while not m_scommessa.isdigit():
                m_scommessa = input("Devi inserire un numero: ")
            scommessa += int(m_scommessa)
    print()
    time.sleep(1.5)
    print(f"La tua scommessa ammonta a {scommessa} euro")
    print()
    time.sleep(1.5)
    print("Il banco sta mischiando le carte...")
    print()
