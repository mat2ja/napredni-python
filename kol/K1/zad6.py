'''
U datoteci kocka.txt nalazi se niz skupina brojeva koji su rezultat bacanja kocke. Svaka skupina od 5 znamenki odvojena je zarezom. Datoteka ima sljedeći format:

# ...,###...,###...,###...,###... ###...,###...,###...,###...,###... ###...,###...,###...,###...,###... ...

Svaki redak je jedna skupina, a u svakoj skupini nalazi se pet nizova (odvojenih zarezom) od pet znamenki između 1 i 6.

Napišite program u Pythonu koji će dati odgovor na sljedeće pitanje: Koliko je skupina u ovoj datoteci koje sadrže barem jedan niz u kojem se broj 6 pojavljuje više puta od svih drugih brojeva u tom nizu (ili je jedini broj u nizu)?

Na primjer, neka se datoteka sastoji od sljedeće tri skupine:

45461,52666,61633,31366,21621
44466,64443,56653,24466,16413
43414,66666,44241,56545,46623

Ovdje postoje dvije skupine gdje se znamenka 6 pojavljuje više od svih drugih: prva skupina u drugom nizu i treća skupina u drugom i petom nizu, pa bi stoga odgovor bio 2 jer se broj 6 pojavljuje kao najčešći broj u dvije skupine.
'''

f = open(r'files/kocka.txt', 'r')
skupine = [red[:-1].split(',') for red in f]


def is_most_frequent(text, fav):
    frequencies = {}
    for n in text:
        if n in frequencies:
            frequencies[n] += 1
        else:
            frequencies[n] = 1

    keys = frequencies.keys()
    values = frequencies.values()

    # nema nijedne sestice
    if fav not in keys:
        return False

    # ako je samo jedan broj (sve su setice)
    if len(keys) == 1:
        return True

    max_count = max(values)
    # ako ima samo jedna max value, i ako je bas to freq sestice
    if list(values).count(max_count) == 1 and frequencies[fav] == max_count:
        return True

    return False


def find_highest_groups(skupine, n):
    counter = 0
    for skupina in skupine:
        najvise_sestica = any(is_most_frequent(niz, n) for niz in skupina)
        if (najvise_sestica):
            counter += 1
    return counter


print(find_highest_groups(skupine, '6'))  # 448
