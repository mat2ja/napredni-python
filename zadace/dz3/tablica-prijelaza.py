class Automat:
    def __init__(self, tekst, dijag_pr):
        self.tekst = tekst
        self.dijag_pr = dijag_pr

    def pokreni(self):
        # Upotreba lokalne funkcije da se ne moraju
        # zadavati parametri .
        def _prep(stanje, tekst, razmak=0):
            print(' ' * razmak, (stanje, tekst))
            if tekst == '':
                if stanje == 'K':
                    return True
                else:
                    return False
            else:
                znak = tekst[0]

                # Ako postoji prelaz za tekuce stanje i znak ...
                if (stanje in self.dijag_pr and znak in self.dijag_pr[stanje]):
                    # Za sva stanja u koja se moze ici za tekuci znak (NFA)

                    for st in self.dijag_pr[stanje][znak]:
                        if _prep(st, tekst[1:], razmak + 4):
                            return True
                    # nijedan izbor stanja nije uspio
                    return False
                else:
                    return False
        return _prep(0, self.tekst)


def test():
    '''
    Primjer automata za regularni izraz (a|b)*abb
    '''
    prijelazi = {
        0: {'a': {0, 1}, 'b': {0}},
        1: {'b': {2}},
        2: {'b': {'K'}}
    }

    tekst = 'aababb'
    print('Ulazni string :', tekst)
    auto = Automat(tekst, prijelazi)

    r = auto.pokreni()
    print(r)


test()


'''
 (0, 'aababb')
     (0, 'ababb')
         (0, 'babb')
             (0, 'abb')
                 (0, 'bb')
                     (0, 'b')
                         (0, '')
                 (1, 'bb')
                     (2, 'b')
                         ('K', '')
'''