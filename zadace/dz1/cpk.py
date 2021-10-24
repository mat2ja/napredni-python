from implementacija_grafa import Cvor,  Boja


'''
Čvrsto pretraživanje komponente

Čvrsto povezana komponenta usmjerenog grafa G = (V, E) je najveći podskup čvorova C ⊆ V takav da se za svaki par čvorova u i v u C može od u doći do v i obratno.
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
        c: [f, d],
        d: [a],
        e: [c],
        f: [g],
        g: [h, f],
        h: [g],
    }

    print(cpk(graf))


test_cpk()

'''
[{c, d, e, a, b}, {g, h, f}]
'''
