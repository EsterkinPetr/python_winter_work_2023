sp = [1, 2, 5, 6, 7, 9, 10, -2, -3, -2, -1, 0]
np = []
for i in range(- len(sp), -2):
    if sp[i + 1] - sp[i] != 1:
        np.append(sp[i + 1])
print(np)