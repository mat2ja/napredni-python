'''
U datoteci intervali.txt nalazi se popis brojeva veličine između 10 i 1000000.
Svaki od tih brojeva pripada odgovarajućem intervalu. Interval kojem pripada
broj određuje se na osnovu početne znamenke i broja znamenki. Na primjer, broj
529 pripada intervalu 500-599, broj 10209 intervalu 10000-19999, a broj 1618
intervalu 1000-1999.

Napišite program u Pythonu koji će dati odgovor na sljedeće pitanje: Koji je
ukupan broj intervala kojima pripada više od 100 brojeva?
'''

f = open(r'files/intervali.txt', 'r')
redovi = [red[:-1] for red in f]


intervali = {}


def mapiraj_intervale(brojevi):
    intervali = {}

    for broj in brojevi:
        prvi = broj[0]
        duljina = len(broj)
        start = prvi.ljust(duljina, '0')
        end = prvi.ljust(duljina, '9')
        interval = (start, end)

        if interval in intervali:
            intervali[interval] += 1
        else:
            intervali[interval] = 1

    return intervali


def broji_intervale(brojevi, quota=100):
    intervali = mapiraj_intervale(brojevi)
    count = len([count for count in intervali.values() if count > quota])
    return count


print(broji_intervale(redovi))
