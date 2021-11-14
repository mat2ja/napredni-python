import re

s = 'abbb '
r1 = 'a*b'
rezultat = re.match(r1, s)
print('1)', r1, ':', s, '->', rezultat)

s = 'aaab'
r2 = 'a*b'
rezultat = re.match(r2, s)
print('2)', r2, ':', s, '->', rezultat)

s = 'xyzaaaabwww'
rezultat = re.match(r2, s)
print('3)', r2, ':', s, '->', rezultat)

s = 'aaaabwww'
rezultat = re.match(r2, s)
print('4)', r2, ':', s, '->', rezultat)

s = 'xyzaaaabwww'
rezultat = re.search(r2, s)
print('5)', r2, ':', s, '->', rezultat)

s = '4.11.2019.'
r3 = r'[0-9]{1,2}.[0 -9]{1,2}.[0-9]{4}.'
# r3 = r'[\d]{1,2}.[\d]{1,2}.[\d]{4}.'

rezultat = re.match(r3, s)
print('6)', r3, ':', s, '->', rezultat)

s = 'baabb'
r4 = r'(a | b)*abb'
rezultat = re.match(r4, s)
print('7)', r4, ':', s, '->', rezultat)

s = 'dana 4.11.2019. odrzana je konferencija'
rezultat = re. search(r3, s)
print('8)', r3, ':', s, '->', rezultat)
