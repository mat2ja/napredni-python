'''
# 1.zadatak
U datoteci rotacije.txt nalazi se niz stringova. Jedna rotacija stringa u desno
je prebacivanje posljednjeg znaka tog stringa s kraja na početak. Na primjer,
string 'abcde' rotiran tri puta u desno daje 'cdeab', a isti string rotiran
sedam puta u desno daje 'deabc', što se vidi u samom postupku rotacije:
0: abcde
1: eabcd
2: deabc
3: cdeab
4: bcdea
5: abcde
6: eabcd
7: deabc

Napišite program u Pythonu koji će dati odgovor na sljedeće pitanje: Ako svaki
string pretvorimo u binarni broj tako da je slovo s parnim ASCII kodom 0, a
neparnim 1, te svaki takav niz rotiramo tako da dobijemo najveći mogući broj,
koji je najveći broj koji na taj način možemo dobiti od svih stringova u datoteci?

Na primjer, neka se datoteka sastoji od sljedećih stringova:

ABB
HDGGCT
CCBC

Iz ovih stringova možemo dobiti sljedeće rotacije (prikazane kao liste binarnih
brojeva pored kojih se nalazi decimalni prikaz tog binarnog broja):

Redak: ABB

    ['0', '1', '0'] 2
    ['0', '0', '1'] 1
    ['1', '0', '0'] 4
Redak: HDGGCT

    ['0', '0', '0', '1', '1', '1'] 7
    ['1', '0', '0', '0', '1', '1'] 35
    ['1', '1', '0', '0', '0', '1'] 49
    ['1', '1', '1', '0', '0', '0'] 56
    ['0', '1', '1', '1', '0', '0'] 28
    ['0', '0', '1', '1', '1', '0'] 14
Redak: CCBC

    ['1', '1', '1', '0'] 14
    ['0', '1', '1', '1'] 7
    ['1', '0', '1', '1'] 11
    ['1', '1', '0', '1'] 13

Iz ovog bi odgovor bio 56 jer to je najveći broj koji možemo dobiti iz ove datoteke
stringova. Za konverziju broja iz binarnog u decimalni oblik možete koristiti funkciju
(klasu) int (primjerice, int('1101', 2) daje 13).
'''


f = open(r'files/rotacije.txt', 'r')
redovi = [red[:-1] for red in f]

# redovi = ['ABBA', 'HDGGCT', 'CCBC']


def shift_right(arg, amount=1):
    return arg[-amount:] + arg[:-amount]


def binary2decimal(n_bin):
    return int(n_bin, 2)


def str2binary(str):
    # pretvori string redove u array binarnih, i pretvori ga string
    return ''.join(['0' if ord(ch) % 2 == 0 else '1'
                    for ch in str])


def get_all_combinations(str):
    # stvori array kombinacije binarya u stringu
    return [''.join(shift_right(str, i)) for i in range(len(str))]


def get_max_value(redovi):
    binary_redovi = [str2binary(red) for red in redovi]

    max_num = 0
    for binary_red in binary_redovi:
        combos = get_all_combinations(binary_red)
        local_max = max([binary2decimal(combo) for combo in combos])
        max_num = max(max_num, local_max)

    return max_num


print(get_max_value(redovi))
