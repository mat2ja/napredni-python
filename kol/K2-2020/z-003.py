'''U modulu b2.py nalazi se lista 'podaci' koja sadrži niz podlista(to jest,
koja je strukturirana kao[[...], [...], ..., [...]].

Napišite program u Pythonu koji će dati odgovor na sljedeće pitanje: Uzevši u
obzir sve podliste(i njihove podliste) liste 'podaci', koji je ukupan broj
podlista koje se sastoje od točno dva broja gdje je prvi broj manji od drugog?

Na primjer, u listi['z', ['abc', [17, 'b', [[4, 8]], 2], [4, 8, 7, 'x']]] postoji
jedna takva podlista, [4, 8]'''


def prebroji(izraz, rez=0):

    znakovi = [znak for znak in izraz]

    if (len(znakovi) == 2):
        [prvi, drugi] = znakovi

        if str(prvi).isdigit() and str(drugi).isdigit() and prvi < drugi:
            return rez + 1

    for i in range(len(znakovi)):
        if isinstance(znakovi[i], list):
            rez = prebroji(znakovi[i], rez)

    return rez


b = prebroji(['z', ['abc', [17, 'b', [[4, 8]], 2], [4, 8, 7, 'x']]]) # 1
print('broj:', b)
