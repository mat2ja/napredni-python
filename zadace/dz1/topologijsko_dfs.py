from implementacija_grafa import Cvor, DFSCvor, Boja

'''
TOPOLOGIJSKO-SORTIRANJE(G)
1. pozovi DFS(G) da bi se dobila završna vremena za svaki čvor
2. u trenutku kada je čvor završen (postavljen na crno) dodaj ga na kraj liste
3. ispiši čvorove liste od kraja prema početku
'''


def dfs2(graf: dict[DFSCvor, set[DFSCvor]]) -> list[Cvor]:
    vrijeme = 0

    # lista cvorova u poretku zacrnjenja
    lista_cvorova: list[Cvor] = []

    def dfs_prolaz(polazni_cvor: DFSCvor) -> None:
        nonlocal vrijeme, lista_cvorova
        vrijeme += 1
        polazni_cvor.otkriven = vrijeme
        polazni_cvor.boja = Boja.Siva
        for cvor in graf[polazni_cvor]:
            if cvor.boja == Boja.Bijela:
                cvor.prethodnik = polazni_cvor
                dfs_prolaz(cvor)

        polazni_cvor.boja = Boja.Crna
        vrijeme += 1
        polazni_cvor. zavrsen = vrijeme

        # dodaj zacrnjeni cvor u listu
        lista_cvorova += [polazni_cvor]

    def main() -> None:
        for cvor in graf:
            if cvor.boja == Boja.Bijela:
                dfs_prolaz(cvor)

    main()
    return lista_cvorova


def test_sort():
    v1 = DFSCvor('v1')
    v2 = DFSCvor('v2')
    v3 = DFSCvor('v3')
    v4 = DFSCvor('v4')
    v5 = DFSCvor('v5')
    v6 = DFSCvor('v6')
    v7 = DFSCvor('v7')

    graf: dict[DFSCvor, set[DFSCvor]] = {
        v1: {v2, v3, v4},
        v2: {v4, v5},
        v3: {v6},
        v4: {v3, v6, v7},
        v5: {v4, v7},
        v6: set(),
        v7: {v6}
    }

    r = dfs2(graf)
    print([c.naziv for c in reversed(r)])


test_sort()

'''
Funkcija dfs2 dati će isti rezultat kao i funkcija topologijski_sort.
'''
