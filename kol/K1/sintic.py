# U datoteci sifre.txt nalazi se niz stringova koji se sastoje samo od malih
# slova. Te stringove treba transformirati na sljedeći način: ASCII kod svakog
# slova treba umanjiti za 10. Ako je rezultat manji od 97 (malo slovo 'a') onda
# treba umanjivanje nastaviti od kraja (to jest, od slova 'z'). Na primjer, slovo
# 'e' umanjeno za 10 daje slovo 'u'.
#
# Napišite program u Pythonu koji će dati odgovor na sljedeće pitanje: Koliko
# stringova u datoteci sifre.txt nakon transformacije sadrži barem jedno od slova
# a, e, i, o ili u?

print("sifre:")


def sifre(st):
    lista = []
    slova = 'aeiou'
    for slovo in st:
        if ord(slovo)-10 >= 97:
            lista.append(chr(ord(slovo)-10))
        else:
            lista.append(chr(ord(slovo)-10+26))

    postoji_li = any(item in lista for item in slova)
    return postoji_li


zbroj = 0

for red in open(r'files/sifre.txt', 'r'):
    if sifre(red[:-1]):
        zbroj += 1


print(zbroj)


# U datoteci tekst.txt nalazi se niz stringova. Napišite program u Pythonu koji
# će dati odgovor na sljedeće pitanje: Koja je najveća duljina podniza u kojem se
# jedno slovo uzastopno ponavlja?
# Na primjer, za niz stringova
#
# aabbcccccddaa
# hhtttvvvvvvvvvvvvvvvvvviiiihhhhh
# aarrrrree
# ccciiiiiiiiiiiiiiiiiikkkkeeee
#
# najduže ponavljanje je 18 jer se slova 'v' i 'i' ponavljaju 18 puta ('v' u
# drugom, a 'i' u četvrtom stringu), što je više od uzastopnog ponavljanja bilo
# kojeg drugog slova u gornjem nizu stringova. Nije važno o kojem slovu ili slovima
# se radi, nego samo koja je najveća duljina ponavljanja.

print("tekst:")


def najdulji(st):
    najduzi = []
    trenutni = []

    trenutni.append(st[0])

    for slovo in st[1:]:
        if slovo == trenutni[0]:
            trenutni.append(slovo)
        else:
            if len(najduzi) < len(trenutni):
                najduzi = trenutni
            trenutni = [slovo]
    return len(najduzi)


maximalni = 0

for red in open(r'files/tekst.txt', 'r'):
    najdulji_u_stringu = najdulji(red[:-1])

    if najdulji_u_stringu > maximalni:
        maximalni = najdulji_u_stringu

print(maximalni)

# U datoteci intervali.txt nalazi se popis brojeva veličine između 10 i 1000000.
# Svaki od tih brojeva pripada odgovarajućem intervalu. Interval kojem pripada
# broj određuje se na osnovu početne znamenke i broja znamenki. Na primjer, broj
# 529 pripada intervalu 500-599, broj 10209 intervalu 10000-19999, a broj 1618
# intervalu 1000-1999.
#
# Napišite program u Pythonu koji će dati odgovor na sljedeće pitanje: Koji je
# ukupan broj intervala kojima pripada više od 100 brojeva?

print("intervali:")


def interval(str):
    interval = str[0] + (len(str) - 1) * '0'
    return interval


mapa = {}
veci_od_sto = 0

for red in open(r'files/intervali.txt', 'r'):
    trenutni = interval(red)

    if trenutni in mapa.keys():
        mapa[trenutni] += 1
    else:
        mapa[trenutni] = 1

for k, v in mapa.items():
    if v > 100:
        veci_od_sto += 1

print(veci_od_sto)


# Datoteka konverzija.txt sastoji se od rimskih i decimalnih cijelih pozitivnih brojeva.
# Rimski broj sastoji se od sljedećih slova (u zagradi je vrijednost tog slova): M (1000),
# D (500), C (100), L (50), X (10), V (5) i I (1). Vrijednost rimskog broja dobijemo tako da
# zbrojimo vrijednosti pojedinačnih slova. Zbog jednostavnosti oduzimanje ćemo ignorirati.
# Na primjer, MDXVII je broj 1517: 1000(M)+500(D)+10(X)+5(V)+1(I)+1(I). Isto tako, MV je
# 1005. Iako bi broj kao što je 7 mogli prikazati sa sedam znakova I, to jest, IIIIIII,
# najkraći zapis bio bi sa 5 + 2, to jest, VII. Isto tako, broj 4 bio bi napisan kao IIII,
# ne IV jer nema oduzimanja (IV je 5 - 1). Devet bi bilo VIIII (5 + 4, ne IX što bi bilo
# 10 - 1). Ovdje podrazumijevamo takav zapis rimskih brojeva.
# Na sličan način možemo decimalni broj konvertirati u rimski. Na primjer, za broj 1517
# dobili bi MDXVII tako da krenemo od najveće rimske znamenke čija vrijednost je manja od
# trenutnog broja, što je M (1000), i to oduzmemo od preostalog broja, nakon čega nam je
# ostalo 517. Najveća rimska znamenka koju sada možemo upotrijebiti je D (500), nakon čega
# nam ostaje 17. Po istom principu iduća znamenka je X (10), što ostavlja 7, pa je iduća
# znamenka V (5), te na kraju II za 2. Na isti način, za broj 2517 dobili bi MMDXVII (dva
# M za dvije tisuće).
#
# Napišite program u Pythonu koji će dati odgovor na sljedeće pitanje: Koji je najmanji broj
# znakova u koji možemo transformirati sadržaj ove datoteke tako da napravimo jedno od
# sljedećeg:
# * transformiramo sve rimske brojeve u decimalne, ILI
# * transformiramo sve decimalne brojeve u rimske (u prethodno opisan oblik)?

print("konverzija:")


def u_arapske(st):
    broj = 0
    for znak in st:
        if znak == 'M':
            broj += 1000
        elif znak == 'D':
            broj += 500
        elif znak == 'C':
            broj += 100
        elif znak == 'L':
            broj += 50
        elif znak == 'X':
            broj += 10
        elif znak == 'V':
            broj += 5
        elif broj > 1:
            broj += 1
    return str(broj)


def u_rimske(st):
    broj = int(st)
    rimski = 'r'

    while (broj > 0):
        if broj >= 1000:
            broj -= 1000
            rimski += 'M'
        elif broj >= 500:
            broj -= 500
            rimski += 'D'
        elif broj >= 100:
            broj -= 100
            rimski += 'C'
        elif broj >= 50:
            broj -= 50
            rimski += 'L'
        elif broj >= 10:
            broj -= 10
            rimski += 'X'
        elif broj >= 5:
            broj -= 5
            rimski += 'V'
        else:
            broj -= 1
            rimski += 'I'
    rimski = rimski[1:]
    return rimski


def transformiraj(st, brojevi):
    if st.isnumeric():
        brojevi['arapski'] += len(st)
        brojevi['rimski'] += len(u_rimske(st))
    else:
        brojevi['rimski'] += len(st)
        brojevi['arapski'] += len(u_arapske(st))
    return brojevi


brojevi = {'rimski': 0, 'arapski': 0}


for red in open(r'files/konverzija.txt', 'r'):
    brojevi = transformiraj(red[:-1], brojevi)
    print(brojevi)

if brojevi['rimski'] < brojevi['arapski']:
    print(brojevi['rimski'])
else:
    print(brojevi['arapski'])
