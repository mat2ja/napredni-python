'''
5. Neka postoji projekt koji se sastoji od N aktivnosti gdje jedna ili više aktivnosti
moraju biti odrađene prije jedne ili više drugih aktivnosti. Napišite program za
koji se upotrebom grafova može definirati ovakav skup aktivnosti i koji će ispisati
prihvatljivi redoslijed izvođenja tih aktivnosti tako da je zadovoljen njihov zadani
redoslijed. NAPOMENA: Skicirajte jedan primjer grafa za ovaj problem
'''

from functools import reduce


from implementacija_grafa import Cvor


def poredak_aktivnosti(graf: dict[Cvor, set[Cvor]]) -> list[str]:
    rezultat: list[str] = []
    while len(graf):
        cvor = set(graf) - reduce(lambda x, y: x | y, graf.values())
        pocetni = cvor.pop()
        rezultat.append(pocetni.naziv)
        del graf[pocetni]
    return reversed(rezultat)


def test_poredak():
    v1 = Cvor('v1')
    v2 = Cvor('v2')
    v3 = Cvor('v3')
    v4 = Cvor('v4')
    v5 = Cvor('v5')
    v6 = Cvor('v6')
    v7 = Cvor('v7')

    graf_1: dict[Cvor, set[Cvor]] = {
        v1: set(),
        v2: set(),
        v3: {v1, v2},
        v4: {v2}, 
        v5: {v2, v4},
        v6: {v5, v7},
        v7: {v3}
    }

    r1 = poredak_aktivnosti(graf_1)
    print('GRAF #1')
    print(*[cvor for cvor in r1], sep=" → ")

    graf_1: dict[Cvor, set[Cvor]] = {
        v1: {v4, v7},
        v2: {v1, v7},
        v3: {v4},
        v4: set(),
        v5: {v3, v6, v4},
        v6: {v2, v3},
        v7: set()
    }

    r2 = poredak_aktivnosti(graf_1)
    print('GRAF #2')
    print(*[cvor for cvor in r2], sep=" → ")


test_poredak()
