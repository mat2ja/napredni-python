from implementacija_grafa import Cvor, BFSCvor, Boja, Queue
from typing import Union
import math


def optimalni_put(graf: dict[Cvor, set[Cvor]], polazni_cvor: Cvor, odredisni_cvor: Cvor):
    min_uk_vrij = math.inf
    putevi: list[(set[Cvor], int)]
    tren_cvor = polazni_cvor
    while tren_cvor != odredisni_cvor:
        for cvor in graf[tren_cvor]:
            cvor.prethodnik = tren_cvor
            tren_cvor = cvor
    print(tren_cvor)
    if (tren_cvor == odredisni_cvor):
        pass


def test_fn():
    u = BFSCvor('u')
    v = BFSCvor('v')
    w = BFSCvor('w')
    x = BFSCvor('x')
    y = BFSCvor('y')
    z = BFSCvor('z')

    graf: dict[BFSCvor, set[(BFSCvor, int)]] = {
        u: {(v, 32), (x, 74)},
        v: {(y, 42)},
        w: {(y, 57), (z, 10)},
        x: {(v, 77)},
        y: {(x, 20)},
        z: {(z, 17)},
    }

    putevi = optimalni_put(graf, u, y)
    print(putevi)


test_fn()
