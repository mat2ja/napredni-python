from implementacija_grafa import Cvor,  Boja

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

    print('Ima ciklus:', ima_ciklus(graf))


test_cpk()
