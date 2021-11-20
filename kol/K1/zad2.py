'''
# 2.zadatak
U datoteci sifre.txt nalazi se niz stringova koji se sastoje samo od malih
slova. Te stringove treba transformirati na sljedeći način: ASCII kood svakog
slova treba umanjiti za 10. Ako je rezultat manji od 97 (malo slovo 'a') onda
treba umanjivanje nastaviti od kraja (to jest, od slova 'z'). Na primjer, slovo
'e' umanjeno za 10 daje slovo 'u'.

Napišite program u Pythonu koji će dati odgovor na sljedeće pitanje: Koliko
stringova u datoteci sifre.txt nakon transformacije sadrži barem jedno od slova
a, e, i, o ili u?
'''

import re

f = open(r'files/sifre.txt', 'r')
redovi = [red[:-1] for red in f]


def umanji(char):
    value = ord(char)
    umanjeno = value - 10
    if (umanjeno < ord('a')):
        razlika = ord('a') - umanjeno
        umanjeno = (ord('z') + 1) - razlika
    return chr(umanjeno)


def transformiraj(redovi):
    transformirano = []
    for sifra in redovi:
        nova_sifra = ''.join([umanji(ch) for ch in sifra])
        transformirano.append(nova_sifra)
    return transformirano


def count_with_vowels(sifre):
    counter = 0
    for sifra in sifre:
        has_vowel = re.search(r'[aeiou]', sifra)
        if has_vowel:
            counter += 1
    return counter


transformirano = transformiraj(redovi)

print(count_with_vowels(transformirano))
