'''
1. Napišite funkciju vrijednost koja za zadani izraz u prefiksnom obliku zadanom kao
Pythonova lista daje rezultat tog izraza. Na primjer, vrijednost izraza [mnozi,
2, 7] je 14 ako je funkcija mnozi definirana tako da pomnozi dvije vrijednosti.
Slično, funkcija zbroji daje zbroj svojih parametara.

a) Definirajte funkcije mnozi i zbroji tako da rade s točno 2 parametra.
x = [mnozi, 2, [mnozi, [zbroji, [zbroji, 2, 1], 7], [mnozi , 4, 2]]]

b) Definirajte ove funkcije tako da rade s bilo kojim brojem parametara.
x = [mnozi , 2, 3, [zbroji , 1, 2, 3, 4]]
'''

aritmetika = {
    'mnozi': lambda x, y: x * y,
    'zbroji': lambda x, y: x + y
}


def izracunaj_a(izraz, rez=0):
    operacija = izraz[0]
    lijevo = izraz[1]
    desno = izraz[2]

    if isinstance(lijevo, list):
        lijevo = izracunaj_a(lijevo, rez)

    if isinstance(desno, list):
        desno = izracunaj_a(desno, rez)

    if not isinstance(lijevo, list) and not isinstance(desno, list):
        rez = aritmetika[operacija](lijevo, desno)

    return rez


a = izracunaj_a(
    ['mnozi', 2, ['mnozi', ['zbroji', ['zbroji', 2, 1], 7], ['mnozi', 4, 2]]])
print('a)', a)


def izracunaj_b(izraz, rez=0):
    operacija = izraz[0]
    brojevi = [broj for broj in izraz[1:]]
    for i in range(len(brojevi)):
        if isinstance(brojevi[i], list):
            brojevi[i] = izracunaj_b(brojevi[i], rez)

    for i in range(len(brojevi)-1):
        brojevi[i+1] = aritmetika[operacija](brojevi[i], brojevi[i+1])
    rez = brojevi[i+1]

    return rez


b = izracunaj_b(['mnozi', 2, 3, ['zbroji', 1, 2, 3, 4]])
print('b)', b)
