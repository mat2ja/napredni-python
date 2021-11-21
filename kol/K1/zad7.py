'''
Datoteka konverzija.txt sastoji se od rimskih i decimalnih cijelih pozitivnih brojeva.
Rimski broj sastoji se od sljedećih slova (u zagradi je vrijednost tog slova):
M (1000), D (500), C (100), L (50), X (10), V (5) i I (1).
Vrijednost rimskog broja dobijemo tako da zbrojimo vrijednosti pojedinačnih slova.
Zbog jednostavnosti oduzimanje ćemo ignorirati.

Na primjer, MDXVII je broj 1517: 1000(M)+500(D)+10(X)+5(V)+1(I)+1(I).
Isto tako, MV je 1005. Iako bi broj kao što je 7 mogli prikazati sa sedam znakova I, to jest, IIIIIII,
najkraći zapis bio bi sa 5 + 2, to jest, VII. Isto tako, broj 4 bio bi napisan kao IIII, ne IV jer nema oduzimanja (IV je 5 - 1).
Devet bi bilo VIIII (5 + 4, ne IX što bi bilo 10 - 1). Ovdje podrazumijevamo takav zapis rimskih brojeva.

Na sličan način možemo decimalni broj konvertirati u rimski. Na primjer, za broj 1517
dobili bi MDXVII tako da krenemo od najveće rimske znamenke čija vrijednost je manja od
trenutnog broja, što je M (1000), i to oduzmemo od preostalog broja, nakon čega nam je
ostalo 517. Najveća rimska znamenka koju sada možemo upotrijebiti je D (500), nakon čega
nam ostaje 17. Po istom principu iduća znamenka je X (10), što ostavlja 7, pa je iduća
znamenka V (5), te na kraju II za 2. Na isti način, za broj 2517 dobili bi MMDXVII (dva
M za dvije tisuće).

Napišite program u Pythonu koji će dati odgovor na sljedeće pitanje: Koji je najmanji broj
znakova u koji možemo transformirati sadržaj ove datoteke tako da napravimo jedno od
sljedećeg:
* transformiramo sve rimske brojeve u decimalne, ILI
* transformiramo sve decimalne brojeve u rimske (u prethodno opisan oblik)?
'''


f = open(r'files/konverzija.txt', 'r')
redovi = [red[:-1] for red in f]


# redovi = ['923', '95', 'CCCCLXXXV', 'DCCLVII']


roman_dict = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}


def roman_to_decimal_str(roman):
    return str(sum([roman_dict[char] for char in roman]))


def decimal_to_roman(decimal):
    n = int(decimal)
    roman = ''
    for key, value in roman_dict.items():
        while n >= value:
            n -= value
            roman += key
    return roman


def sum_lengths(redovi):
    return sum([len(broj) for broj in redovi])


def sum_len_decimal(redovi):
    brojevi = [roman_to_decimal_str(red) if not red.isnumeric()
               else red for red in redovi]
    return sum_lengths(brojevi)


def sum_len_roman(redovi):
    rimski = [decimal_to_roman(red) if red.isnumeric()
              else red for red in redovi]
    return sum_lengths(rimski)


def calc_min_chars(redovi):
    duljina_decimalnih = sum_len_decimal(redovi)
    duljina_rimskih = sum_len_roman(redovi)
    return min(duljina_decimalnih, duljina_rimskih)


print(calc_min_chars(redovi))
