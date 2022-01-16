'''
Matija Osrečki
'''
import re

'''
ZADATAK 1
Najveca duljina podniza u kojem se jedno slovo uzastopno ponavlja?
'''
f_1 = open(r'files/tekst.txt', 'r')
redovi_1 = [red[:-1] for red in f_1]


def naj_ponavljanje(redovi):
    max_repeat = 1
    for red in redovi:
        local_repeat = 1
        for i in range(1, len(red)):
            if red[i-1] == red[i]:
                local_repeat += 1
                max_repeat = max(max_repeat, local_repeat)
            else:
                local_repeat = 1

    return max_repeat


print('1) tekst:', naj_ponavljanje(redovi_1))  # 25


'''
ZADATAK 2
Ukupan broj intervala kojima pripada više od 100 brojeva?
'''
f_2 = open(r'files/intervali.txt', 'r')
redovi_2 = [red[:-1] for red in f_2]


def mapiraj_intervale(brojevi):
    intervali = {}

    for broj in brojevi:
        prvi = broj[0]
        duljina = len(broj)
        start = prvi.ljust(duljina, '0')
        end = prvi.ljust(duljina, '9')
        interval = (start, end)

        if interval in intervali:
            intervali[interval] += 1
        else:
            intervali[interval] = 1

    return intervali


def broji_intervale(brojevi, quota=100):
    intervali = mapiraj_intervale(brojevi)
    return len([count for count in intervali.values() if count > quota])


print('2) intervali:', broji_intervale(redovi_2))  # 7


'''
ZADATAK 3
Koje je najmanje odstupanje stringa 'piramida'?
(izračunati apsolutnu razliku ASCII koda tog slova sa ASCII kodom slova na istoj poziciji stringa)
'''
f_3 = open(r'files/stringovi.txt', 'r')
redovi_3 = [red[:-1] for red in f_3]

zadani_string = 'piramida'


def odstupanje_znakova(a, b):
    return abs(ord(a) - ord(b))


def suma_odstupanja_reda(red, main_str):
    duljina = len(main_str)
    red = red.ljust(duljina)
    odstupanja = [odstupanje_znakova(main_str[i], red[i])
                  for i in range(duljina)]
    return sum(odstupanja)


def min_odstupanje_od(main_str, redovi):
    odstupanja = [suma_odstupanja_reda(red, main_str) for red in redovi]
    return min(odstupanja)


print('3) stringovi:', min_odstupanje_od(zadani_string, redovi_3))  # 145


'''
ZADATAK 4
ASCII kod svakog slova treba umanjiti za 10. 
Ako je rezultat manji od 97 (malo slovo 'a') onda treba umanjivanje nastaviti od kraja (to jest, od slova 'z')
Koliko stringova u datoteci sifre.txt nakon transformacije sadrži barem jedno od slova a, e, i, o ili u?
'''
f_4 = open(r'files/sifre.txt', 'r')
redovi_4 = [red[:-1] for red in f_4]


def umanji(char):
    umanjeno = ord(char) - 10
    if (umanjeno < ord('a')):
        umanjeno = (ord('z') - ord('a') + 1) + umanjeno
    return chr(umanjeno)


def transformiraj_sifre(redovi):
    transformirano = []
    for sifra in redovi:
        nova_sifra = ''.join([umanji(ch) for ch in sifra])
        transformirano.append(nova_sifra)
    return transformirano


def has_vowel(sifra):
    return re.search(r'[aeiou]', sifra)


def count_with_vowels(redovi):
    sifre = transformiraj_sifre(redovi)
    return len([sifra for sifra in sifre if has_vowel(sifra)])


print('4) sifre:', count_with_vowels(redovi_4))  # 2694
