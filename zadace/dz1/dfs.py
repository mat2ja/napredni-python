# type: ignore

from implementacija_grafa import Cvor, DFSCvor, Boja


def dfs(graf: dict[DFSCvor, set[DFSCvor]]) -> None:
    vrijeme = 0

    def dfs_prolaz(polazni_cvor: DFSCvor) -> None:
        nonlocal vrijeme

        vrijeme += 1
        polazni_cvor.otkriven = vrijeme
        polazni_cvor.boja = Boja.Siva
        for cvor in graf[polazni_cvor]:
            if cvor.boja == Boja.Bijela:
                cvor.prethodnik = polazni_cvor
                dfs_prolaz(cvor)

        polazni_cvor.boja = Boja.Crna
        vrijeme += 1
        polazni_cvor.zavrsen = vrijeme

    def main() -> None:
        for cvor in graf:
            if cvor.boja == Boja.Bijela:
                dfs_prolaz(cvor)

    main()


def test_dfs():
    u = DFSCvor('u')
    v = DFSCvor('v')
    w = DFSCvor('w')
    x = DFSCvor('x')
    y = DFSCvor('y')
    z = DFSCvor('z')

    graf: dict[DFSCvor, set[DFSCvor]] = {
        u: {v, x},
        v: {y},
        w: {y, z},
        x: {v},
        y: {x},
        z: {z},
    }

    dfs(graf)

    for cvor in graf:
        print(cvor)

    print('Korijen :', u)
    ispisi_stablo(graf, u)

    print('Korijen :', w)
    ispisi_stablo(graf, w)


def ispisi_stablo(graf, polazni_cvor):
    ispisano = set()

    def dfs_stablo(cvor, dubina=0):
        nonlocal ispisano
        print(' ' * dubina, cvor.naziv)
        # init ispisano if empty, otherwise use ispisano
        ispisano |= {cvor}
        for c in graf[cvor]:
            if c not in ispisano and c.prethodnik == cvor:
                dfs_stablo(c, dubina + 4)

    dfs_stablo(polazni_cvor)


test_dfs()

'''
(u) otkriven / zavrsen : 1/8
(v) otkriven / zavrsen : 2/7
(w) otkriven / zavrsen : 9/12
(x) otkriven / zavrsen : 4/5
(y) otkriven / zavrsen : 3/6
(z) otkriven / zavrsen : 10/11
Korijen : (u) otkriven / zavrsen : 1/8
 u
     v
         y
             x
Korijen : (w) otkriven / zavrsen : 9/12
 w
     z

'''
