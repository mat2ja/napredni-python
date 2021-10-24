from typing import Union
from implementacija_grafa import Cvor, BFSCvor, Boja, Queue

'''
Za graf G=(V, E) i čvor s koji ćemo zvati izvorni čvor, pretraživanje u širinu sistematično ispituje lukove grafa G da bi dobio sve čvorove do kojih se može doći iz s i odredio najkraći put do svakog od tih čvorova.

Ovaj algoritam radi za usmjerene i neusmjerene grafove.

Kao kod stabla, pretraživanje u širinu radi tako da pronađe sve čvorove na udaljenosti d prije nego što pronađe čvorove na udaljenosti d+1.
'''

'''
1. Modificirajte funkciju bfs tako da u težinskom usmjerenom grafu pronađe optimalni put.
Jesu li putevi koje takva funkcija pronalazi uvijek optimalni?
'''


def bfs(graf: dict[Cvor, set[Cvor]], polazni_cvor: Cvor, odredisni_cvor: Cvor) -> list((set[Cvor], int)):
    polazni_cvor.udaljenost = 0

    putevi: list((set[Cvor], int)) = list()

    # {
    #     ({x,y,z}, 30),
    #     ({x,a,b,c,z}, 98)
    # }

    red: Queue[Cvor] = Queue()
    red.put(polazni_cvor)
    while not red.empty():
        u = red.get()
        for cvor, _ in graf[u]:
            print('cvor', cvor.naziv)
            if cvor.boja == Boja.Bijela:
                cvor.boja = Boja.Siva
                cvor.udaljenost = u.udaljenost + 1
                cvor.prethodnik = u
                red.put(cvor)

                if (cvor == odredisni_cvor):
                    ukupna_vrijednost = 0
                    trenutni_cvor = cvor
                    trenutni_put: set[Cvor] = {trenutni_cvor}
                    trenutni_put.add(trenutni_cvor)
                    while trenutni_cvor.prethodnik:
                        trenutna_vrijednost = 0
                        for slj_cvor, vrij in graf[trenutni_cvor.prethodnik]:
                            if slj_cvor == trenutni_cvor:
                                trenutna_vrijednost += vrij
                                break
                        ukupna_vrijednost += trenutna_vrijednost
                        trenutni_cvor = trenutni_cvor.prethodnik
                        # dodaj cvor u trenutni put
                        trenutni_put.add(trenutni_cvor)
                    # dodaj trenutni put u sve puteve
                    putevi.append((trenutni_put, ukupna_vrijednost))
                    for put in trenutni_put:
                        put.boja = Boja.Bijela

        u.boja = Boja.Crna
    return putevi


def test_bfs():
    u = BFSCvor('u')
    v = BFSCvor('v')
    w = BFSCvor('w')
    x = BFSCvor('x')
    y = BFSCvor('y')
    z = BFSCvor('z')

    graf: dict[BFSCvor, set[BFSCvor]] = {
        u: {(v, 32), (x, 74)},
        v: {(y, 42)},
        w: {(y, 57), (z, 10)},
        x: {(v, 77)},
        y: {(x, 20)},
        z: {(z, 17)},
    }

    putevi = bfs(graf, u, y)
    print(putevi)


def ispisi_stablo(graf, polazni_cvor):
    ispisano = set()

    def bfs_stablo(cvor, dubina=0):
        nonlocal ispisano
        print(' ' * dubina, cvor.naziv)
        # init ispisano if empty, otherwise use ispisano
        ispisano |= {cvor}
        for c in graf[cvor]:
            if c not in ispisano and c.prethodnik == cvor:
                bfs_stablo(c, dubina + 4)

    bfs_stablo(polazni_cvor)


test_bfs()

'''
(r) udaljenost : 1
(v) udaljenost : 2
(s) udaljenost : 0
(w) udaljenost : 1
(t) udaljenost : 2
(x) udaljenost : 2
(u) udaljenost : 3
(y) udaljenost : 3

 s
     w
         t
             u
         x
             y
     r
         v
'''
