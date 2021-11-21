'''
# 4. zadatak
U datoteci stringovi.txt nalazi se popis stringova maksimalne duljine 8.
Napišite program u Pythonu koji će dati odgovor na sljedeće pitanje: Koje je 
najmanje odstupanje stringa 'piramida' od stringova u ovoj datoteci ako 
izračunavanje odstupanja radimo na sljedeći način:

Neka je string S neki string iz ove datoteke. Za svako slovo stringa S treba 
izračunati apsolutnu razliku ASCII koda tog slova sa ASCII kodom slova na istoj 
poziciji stringa 'piramida', te na kraju zbrojiti sve razlike. Ako je string S
kraći od 8 onda mu treba dodati razmake na kraj (mozete upotrijebiti funkciju 
ljust; primjerice 'abcd'.ljust(6) bi vratila 'abcd  ').

Na primjer, neka datoteka X sadrži sljedeći niz stringova maksimalne duljine 4: 
ABC
DDD 

Ako nas zanima najmanje odstupanje stringa ABCD od ovih stringova 
onda bi to izračunali na sljedeći način:
ABC i ABCD imaju razliku |65-65|+|66-66|+|67-67|+|32-68|=36. Ovdje smo dodali
razmak (ASCII 32) na kraj stringa ABC da bi bio duljine 4.
Isto tako, DDD i ABCD imaju razliku |68-65|+|68-66|+|68-67|+|32-68|=42.
Dakle, najmanje odstupanje stringa ABCD od stringova u datoteci X je 36.
'''


f = open(r'files/stringovi.txt', 'r')
redovi = [red[:-1] for red in f]

zadani_string = 'piramida'


def odstupanje_znakova(a, b):
    return abs(ord(a) - ord(b))


def suma_odstupanja_reda(red, main_str):
    duljina = len(main_str)
    red = red.ljust(duljina)
    odstupanja = [odstupanje_znakova(main_str[i], red[i])
                  for i in range(duljina)]
    return sum(odstupanja)


def min_odstupanje_od(main_str):
    sume_odstupanja = [suma_odstupanja_reda(red, main_str) for red in redovi]
    return min(sume_odstupanja)


print(min_odstupanje_od(zadani_string))
