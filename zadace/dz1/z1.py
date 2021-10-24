from implementacija_grafa import Cvor, BFSCvor, Boja, Queue
from typing import Union

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


test_bfs()
