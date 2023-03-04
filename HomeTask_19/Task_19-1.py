import itertools
wallet = [50, 100, 200, 500, 1000, 5000]
possumm = []
for su in (itertools.combinations(wallet, 3)):
    possumm.append(sum(list(su)))
print(*possumm)


