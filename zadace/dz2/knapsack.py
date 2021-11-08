import itertools
import time

# ( vrijednost , tezina )
predmeti = {'a': (6, 3), 'b': (7, 3), 'c': (8, 2),
            'd': (9, 5)}

# ( vrijednost , tezina )
predmeti2 = {'a': (6, 3), 'b': (7, 3), 'c': (8, 2),
             'd': (9, 5), 'a2': (6, 3), 'b2': (7, 3), 'c2': (8, 2),
             'd2': (9, 5)}


def nadji_najbolji(maks_tezina):
    kombinacije = []
    for n in range(1, len(predmeti) + 1):
        kombinacije += [p for p in
                        itertools.combinations(predmeti, n)]

    najbolji = (None, 0, 0)
    for k in kombinacije:
        print(k)
        vrijednost = sum(predmeti[p][0] for p in k)
        tezina = sum(predmeti[p][1] for p in k)
        if tezina <= maks_tezina and najbolji[1] < vrijednost:
            najbolji = k, vrijednost, tezina

    return najbolji


start_time = time.time()
print(start_time)
print(nadji_najbolji(5))
print(time.time() - start_time)


def nadji_najbolji2(maks_tezina):
    kombinacije = []
    for n in range(1, len(predmeti) + 1):
        komba = []
        for iter in itertools.combinations(predmeti, n):
            komba += [iter]

        kombinacije += komba

    najbolji = (None, 0, 0)
    for k in kombinacije:
        print(k)
        vrijednost = sum(predmeti[p][0] for p in k)
        tezina = sum(predmeti[p][1] for p in k)
        if tezina <= maks_tezina and najbolji[1] < vrijednost:
            najbolji = k, vrijednost, tezina

    return najbolji


start_time2 = time.time()
print(start_time)
print(nadji_najbolji2(5))
print(time.time() - start_time2)
