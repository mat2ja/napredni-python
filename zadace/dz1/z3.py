from implementacija_grafa import Cvor,  Boja
from typing import Union


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

    ciklusi = cpk(graf)

    print('Najduzi ciklus:', najduzi_ciklus(ciklusi))


test_cpk()


