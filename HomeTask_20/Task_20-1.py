import numpy
import pandas as pd
def summa_dig(dfr):
    spel = []
    spdig = []
    for i in dfr.index:
        for j in dfr.columns:
            spel.append(dfr.loc[i, j])
    print(spel)
    for i in spel:
        #print(f'{i}: {type(i)}')
        if isinstance(i, (int, numpy.int64)):
            spdig.append(i)
    res = sum(spdig)
    return(res)
df = pd.DataFrame({'A':[1,'a', 2, 'b', 3, 'c', 4], 'B': [5, 6, 7, 8, 9, 10, 11], 'C':['d', 'e', 'f', 'g', 'h', 'i', 'j']})
print(df)
sp = summa_dig(df)
print(sp)


