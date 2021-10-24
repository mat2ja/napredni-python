from functools import reduce
from implementacija_grafa import Cvor, Boja


def topologijski_sort(graf: dict[Cvor, set[Cvor]]) -> list[str]:
    rezultat: list[str] = []
    while graf != {}:
        # uzima cvor koji nema ulaz
        cvor = set(graf) - reduce(lambda x, y: x | y, graf.values())
        pocetni = cvor.pop()
        rezultat.append(pocetni.naziv)
        del graf[pocetni]
    return rezultat


def test_sort():
    v1 = Cvor('v1')
    v2 = Cvor('v2')
    v3 = Cvor('v3')
    v4 = Cvor('v4')
    v5 = Cvor('v5')
    v6 = Cvor('v6')
    v7 = Cvor('v7')

    graf: dict[Cvor, set[Cvor]] = {
        v1: {v2, v3, v4},
        v2: {v4, v5},
        v3: {v6},
        v4: {v3, v6, v7},
        v5: {v4, v7},
        v6: set(),
        v7: {v6}
    }

    r = topologijski_sort(graf)
    print(r)


test_sort()
