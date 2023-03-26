def fuu(st):
     spdia = [[int(c) for c in b.split('-')] for b in a.split(',')]
     spo = [i for dia in spdia for i in range(dia[0], dia[1] + 1)]
     return spo
a = '1-2,4-4,3-6'
spnat = fuu(a)
print(spnat)

