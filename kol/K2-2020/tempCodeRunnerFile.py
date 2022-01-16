def izracunaj(izraz, rez=0):
#     operacija = izraz[0]
#     brojevi = [broj for broj in izraz[1:]]

#     for i in range(len(brojevi)):
#         if isinstance(brojevi[i], list):
#             brojevi[i] = izracunaj(brojevi[i], rez)

#     for i in range(len(brojevi)-1):
#         brojevi[i+1] = aritmetika[operacija](brojevi[i], brojevi[i+1])
#     rez = brojevi[i+1]

#     return rez


# b = izracunaj(['+', 1, ['*', 2, 3, 4], 2, 3])  # 30