def dnk_rnk(x):
    dzam = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'}
    rnk = []
    for i in x:
        if i in dzam.keys():
            rnk += dzam[i]
    return rnk
dnk = input()
print(''.join(dnk_rnk(dnk)))
