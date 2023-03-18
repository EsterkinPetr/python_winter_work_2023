import itertools
st = 'aabbccddcc'
#st = 'a'
setpodstr = set()
sppol = []
for r in range(1, len(st) + 1):
    x = itertools.combinations(st, r)
    for i in x:
        setpodstr.add(i)

#print(st)
#print(setpodstr)
for i in setpodstr:
    if i == i[::-1]:
        sppol.append(i)
print(sppol)
mdl = max([len(i) for i in sppol])
print(mdl)
for i in sppol:
    if len(i) == mdl:
        print(f'Палиндром с максимальной длиной = {mdl}: {i} ')



