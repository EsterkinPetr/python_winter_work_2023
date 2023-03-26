spisok = [[1, 5, 3], [2, 44, 1, 4], [3, 3], [256]]
num = '0123456789'
zn = []
sspisok = []
count = 0
spst = list(map(str, spisok))
#print(spst)
for i in range(len(spst)):
    for j in range(len(spst[i])):
        if spst[i][j] in num:
            count += 1
    zn.append(count)
    count = 0
#print(zn)
kor = list(zip(spisok, zn))
#print(kor)
ks = sorted(kor, key=lambda x: x[1])  # Сортированный кортеж
#print(ks)
for i in range(len(ks)):
    sspisok.append(ks[i][0])
#print(sspisok)
ssspisok = []
for el in sspisok:
    ssspisok.append(sorted(el, key=lambda x: -x))
print(ssspisok)


