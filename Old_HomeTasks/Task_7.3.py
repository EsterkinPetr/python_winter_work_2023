def Three_maks(x):
    x = matr
    spel =[]
    for i in range(len(x)):
        for j in range(len(x[i])):
            spel.append(x[i][j])
    mel = set(spel)
    spel2 = list(mel)
    sspel2 = sorted(spel2)
    rez = sspel2[(len(sspel2) -3):]
    return rez
matr = [[1, 6, 3], [4, 5, 4]]
print(Three_maks(matr))
