'''U modulu a3.py nalazi se lista 'podaci' koja sadrži niz podlista (to jest, koja je
strukturirana kao [[...], [...], ..., [...]]. Svaka od tih podlista predstavlja
aritmetički izraz u prefiksnom obliku. Na primjer, izraz ['+', 1, ['*', 2, 3, 4], 2, 3]
izračunava se tako da se prvo izračuna unutrašnji podizraz, odnosno ['*', 2, 3, 4],
koji označava umnožak vrijednosti 2, 3 i 4, pa se dobije 24. Nakon toga se izračuna
vanjski izraz koji je sada ['+', 1, 24, 2, 3], što daje 30, pa je 30 konačni rezultat
tog izraza. Općenito, nakon otvorene zagrade uvijek slijedi jedan od operatora '+' (zbroj),
'-' (razlika), '*' (umnožak) ili '/' (kvocijent), a nakon operatora slijede dva ili više
operanda nad kojima se taj operator primjenjuje.

Napišite program u Pythonu koji će dati odgovor na sljedeće pitanje: Koliko izraza
u listi 'podaci' ima negativan rezultat'''


from z3_podaci import podaci

aritmetika = {
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x / y
}


def izracunaj(izraz, rez=0):
    operacija = izraz[0]
    brojevi = [broj for broj in izraz[1:]]

    # if isinstance(operacija, list):
    #     operacija = operacija[0]
    #     brojevi = [broj for broj in operacija[1:]]

    for i in range(len(brojevi)):
        if isinstance(brojevi[i], list):
            brojevi[i] = izracunaj(brojevi[i], rez)

    for i in range(len(brojevi)-1):
        print(i, rez, operacija)
        brojevi[i+1] = aritmetika[operacija](brojevi[i], brojevi[i+1])
    rez = brojevi[i+1]

    return rez


b = izracunaj(['+', 1, ['*', 2, 3, 4], 2, 3])  # 30
# c = izracunaj(podaci)
print('rjesenje b:', b)
# print('rjesenje c:', c)
