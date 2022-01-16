'''
U modulu b1.py nalazi se lista parova. Neka svaki par oznacava
odnos (prethodnik, sljedbenik). 
Svaki sljedbenik može imati svoje sljedbenike, itd.

Napišite program u Pythonu koji će dati odgovor na sljedeće pitanje: 
Koliko sljedbenika ima 'NBIEFnd'?

Na primjer, ako je lista parova

('petar', 'marko'),
('irena', 'ivan'),
('marko', 'stjepan'),
('ana', 'petra'),
('marko', 'suzana'),
('stjepan', 'marko'),
('ivan', 'marija'),
('suzana', 'josip'),
('stjepan', 'marko')

onda 'petar' ima 4 sljedbenika: 'marko', 'josip', 'stjepan', 'suzana' jer je
'marko' njegov direktni sljedbenik, 'stjepan' je direktni sljedbenik od 'marko
pa je time indirektni sljedbenik od 'petar', itd.

NAPOMENA: Vodite računa o tome da podaci mogu imati kružne zavisnosti! 
U gornjem
primjeru, 'stjepan' je sljedbenik od 'marko', a 'marko' je sljedbenik od'stjepan'.

'''
