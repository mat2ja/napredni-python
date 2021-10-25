from functools import reduce
from implementacija_grafa import Cvor, BFSCvor, Boja
from typing import Union
from queue import Queue


'''
1. Modificirajte funkciju bfs tako da u težinskom usmjerenom grafu pronađe optimalni put.
Jesu li putevi koje takva funkcija pronalazi uvijek optimalni?
'''


def bfs(graf: dict[Cvor, set[Cvor]], polazni_cvor: Cvor, odredisni_cvor: Cvor) -> Union[dict, None]:
    polazni_cvor.udaljenost = 0

    red: Queue[Cvor] = Queue()
    red.put(polazni_cvor)

    while not red.empty():
        u = red.get()
        for cvor in graf[u]:
            if cvor.boja == Boja.Bijela:
                cvor.boja = Boja.Siva
                cvor.udaljenost = u.udaljenost + 1
                cvor.prethodnik = u
                red.put(cvor)

                if (cvor == odredisni_cvor):
                    put: list[Cvor] = []
                    trenutni_cvor = cvor
                    while trenutni_cvor.prethodnik:
                        put.append(trenutni_cvor)
                        trenutni_cvor = trenutni_cvor.prethodnik
                    put.append(trenutni_cvor)
                    put.reverse()

                    return {
                        'put': put,
                        'udaljenost': odredisni_cvor.udaljenost
                    }

        u.boja = Boja.Crna
    return None


def test_bfs():
    s = BFSCvor('s')
    r = BFSCvor('r')
    v = BFSCvor('v')
    w = BFSCvor('w')
    t = BFSCvor('t')
    x = BFSCvor('x')
    u = BFSCvor('u')
    y = BFSCvor('y')

    graf: dict[BFSCvor, set[BFSCvor]] = {
        r: {s, v},
        v: {r},
        s: {r, w},
        w: {s, t, x},
        t: {w, x, u},
        x: {w, t, u, y},
        u: {t, x, y},
        y: {x, u},
    }

    optimalni_put = bfs(graf, r, w)
    print('Optimalni put:', end=" ")
    print(*[i.naziv for i in optimalni_put["put"]], sep=" → ")

    print(f'Udaljenost: {optimalni_put["udaljenost"]}')


print('\nZadatak #1')
test_bfs()


'''
2. Upotrebom implementacije grafa iz ovog dijela napišite program koji će utvrditi postoje li ciklusi u zadanom usmjerenom grafu.
'''


def ima_ciklus(graf: dict[Cvor, list[Cvor]]) -> bool:
    polazni_cvor = None

    def ciklus(trenutni_cvor: Cvor, put: set[Cvor]) -> set[Cvor]:
        if polazni_cvor in put:
            return put
        else:
            for cvor in graf[trenutni_cvor]:
                if cvor not in put:
                    r = ciklus(cvor, put | {cvor})
                    if r:
                        return r
            return set()

    for cvor in graf:
        polazni_cvor = cvor
        r = ciklus(polazni_cvor, set())
        if r:
            return True

    return False


'''
3. Upotrebom implementacije grafa iz ovog dijela napišite program koji će u usmjerenom cikličkom grafu pronaći najdulji ciklus.
'''


def cpk(graf: dict[Cvor, list[Cvor]]) -> list[set[Cvor]]:
    polazni_cvor = None

    def ciklus(trenutni_cvor: Cvor, put: set[Cvor]) -> set[Cvor]:
        if polazni_cvor in put:
            return put
        else:
            for cvor in graf[trenutni_cvor]:
                if cvor not in put:
                    r = ciklus(cvor, put | {cvor})
                    if r:
                        return r

            return set()

    ciklusi: list[set[Cvor]] = []
    for cvor in graf:
        polazni_cvor = cvor
        r = ciklus(polazni_cvor, set())
        if not r:
            r = {polazni_cvor}
        ciklusi += [r]

    komponente: list[set[Cvor]] = []
    for c in ciklusi:
        if not komponente:
            komponente.append(c)
        else:
            promjena = False
            for k in komponente:
                if len(c & k) > 0:
                    k |= c
                    promjena = True

            if not promjena:
                komponente.append(c)

    return komponente


def najduzi_ciklus(ciklusi: list[set[Cvor]]) -> Union[set[Cvor], None]:
    naj_ciklus = max(ciklusi, key=len)
    if (len(naj_ciklus) > 1):
        return naj_ciklus
    return None


def test_cpk():
    a = Cvor('a')
    b = Cvor('b')
    c = Cvor('c')
    d = Cvor('d')
    e = Cvor('e')
    f = Cvor('f')
    g = Cvor('g')
    h = Cvor('h')

    graf: dict[Cvor, list[Cvor]] = {
        a: [b],
        b: [e, c],
        # b: [],
        c: [f, d],
        d: [a],
        e: [c],
        f: [g],
        g: [h, f],
        # g: [],
        h: [g],
    }

    print('\nZadatak #2')
    print('Ima ciklus:', ima_ciklus(graf))

    ciklusi = cpk(graf)

    print('\nZadatak #3')
    print('Najduzi ciklus:', najduzi_ciklus(ciklusi))


test_cpk()

'''
5. Neka postoji projekt koji se sastoji od N aktivnosti gdje jedna ili više aktivnosti
moraju biti odrađene prije jedne ili više drugih aktivnosti. Napišite program za
koji se upotrebom grafova može definirati ovakav skup aktivnosti i koji će ispisati
prihvatljivi redoslijed izvođenja tih aktivnosti tako da je zadovoljen njihov zadani
redoslijed. NAPOMENA: Skicirajte jedan primjer grafa za ovaj problem
'''


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

    print('\nZadatak #5')
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
