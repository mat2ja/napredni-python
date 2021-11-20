'''
# 3. zadatak
U datoteci tekst.txt nalazi se niz stringova. Napišite program u Pythonu koji
će dati odgovor na sljedeće pitanje: Koja je najveća duljina podniza u kojem se
jedno slovo uzastopno ponavlja?
Na primjer, za niz stringova

    aabbcccccddaa
    hhtttvvvvvvvvvvvvvvvvvviiiihhhhh
    aarrrrree
    ccciiiiiiiiiiiiiiiiiikkkkeeee

najduže ponavljanje je 18 jer se slova 'v' i 'i' ponavljaju 18 puta ('v' u
drugom, a 'i' u četvrtom stringu), što je više od uzastopnog ponavljanja bilo
kojeg drugog slova u gornjem nizu stringova. Nije važno o kojem slovu ili slovima
se radi, nego samo koja je najveća duljina ponavljanja.
'''


f = open(r'files/tekst.txt', 'r')
redovi = [red[:-1] for red in f]


def naj_pon(redovi):
    max_repeat = 0
    for red in redovi:
        local_repeat = 1
        for i in range(1, len(red)):
            prev = red[i-1]
            curr = red[i]
            if prev == curr:
                local_repeat += 1
                max_repeat = max(max_repeat, local_repeat)
            else:
                local_repeat = 1

    return max_repeat


print(naj_pon(redovi))
