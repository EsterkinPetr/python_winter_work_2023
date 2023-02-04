spisok = [[1, 5, 3], [2, 44, 1, 4], [3, 3], [256]]
sspisok = sorted(spisok, key=lambda x: len(x))
ssspisok = []
for el in sspisok:
    ssspisok.append(sorted(el, key=lambda x: -x))
print(ssspisok)

