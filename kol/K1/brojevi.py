'''
U datoteci brojevi.txt nalaze se stringovi koji se sastoje od tri broja 
(odvojena znakom ';'). Napišite program u Pythonu koji će dati odgovor na 
sljedeće pitanje: Koji je najveći mogući broj koji se može sastaviti od brojeva 
u svakom od stringova tako da ih se postavi u odgovarajući poredak?

Na primjer, neka datoteka X sadrži sljedeća dva stringa:
5;50;56;
16;78;68;

Za prvi niz najveći broj je 56550 (sastavljen od brojeva prvog niza u poretku
56, 5, 50), a za drugi niz to je 786816. Dakle, najveći broj koji se može
dobiti iz gornjih stringova je 786816.

SAVJET: Možete koristiti funkciju itertools.permutations.
'''
from itertools import permutations

f = open(r'files/brojevi.txt', 'r')
redovi = [red[:-1] for red in f]


def get_number(perm):
    return int(''.join(perm))


def najveci_broj(redovi):
    total_max = 0
    for red in redovi:
        red = red.split(';')[:-1]
        local_max = max([get_number(perm) for perm in permutations(red)])
        total_max = max(total_max, local_max)
    return total_max


print(najveci_broj(redovi))
