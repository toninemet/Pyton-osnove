# while petlja


import random

tajnibroj = random.randint(1,30)

while True:

    pogodi = int(input("pogodi jedan broj između 1 i 30: "))

    if tajnibroj == pogodi:
        print("bravo pogodio si! to je bio broj ",tajnibroj)
        break

    else:
        print("fulao si pokušaj ponovo...")

    print("kraj programa")