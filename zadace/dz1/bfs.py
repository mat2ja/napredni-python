from implementacija_grafa import Cvor, BFSCvor, Boja, Queue


def bfs(graf: dict[Cvor, set[Cvor]], polazni_cvor: Cvor) -> None:
    polazni_cvor.udaljenost = 0
    red: Queue[Cvor] = Queue()
    red.put(polazni_cvor)
    while not red.empty():
        u = red.get()  # removes and returns first elem in queue
        for cvor in graf[u]:
            if cvor.boja == Boja.Bijela:
                cvor.boja = Boja.Siva
                cvor.udaljenost = u.udaljenost + 1
                cvor.prethodnik = u
                red.put(cvor)
        u.boja = Boja.Crna


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

    bfs(graf, s)

    for cvor in graf:
        print(cvor)

    ispisi_stablo(graf, s)


test_bfs()
