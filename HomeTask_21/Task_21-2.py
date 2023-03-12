import numpy as np
def opt_route(matr):
    i = 0
    j = 0
    s = 0
    route = {}
    step = 1
    n = matr.shape[0]
    m = matr.shape[1]
    while True:
        if matr[i][j + 1] < matr[i + 1][j]:
            s += matr[i][j]
            route[step] = (matr[i][j], s)
            #s += matr[i][j]
            j += 1
            if j < m - 1:
                step += 1
            else:
                step += 1
                s += matr[i][j]
                route[step] = (matr[i][j], s)
                while i != n - 1:
                    i += 1
                    step += 1
                    s += matr[i][j]
                    route[step] = (matr[i][j], s)
                break
        else:
            s += matr[i][j]
            route[step] = (matr[i][j], s)
            #s += matr[i][j]
            i += 1
            if i < n - 1:
                step += 1
            else:
                step += 1
                s += matr[i][j]
                route[step] = (matr[i][j], s)
                while j != m - 1:
                    step += 1
                    j += 1
                    s += matr[i][j]
                    route[step] = (matr[i][j], s)
                break
    return route
row = int(input('Кол-во рядов:'))
coll = int(input('Кол-во столбцов:'))
random_matrix = np.random.randint(1, 100, (row, coll))
print(random_matrix)
#print(opt_route(random_matrix))
dor = opt_route(random_matrix)
for k, v in dor.items():
    print(f'шаг {k}: число в клетке: {v[0]}, сумма чисел: {v[1]}')

