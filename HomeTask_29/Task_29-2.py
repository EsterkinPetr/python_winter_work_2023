def rotate(mat, dr):
    if dr == 'acw':
        tmat = [list(i) for i in zip(*mat)]
        #print(tmat)
        res = list(reversed(tmat))
    elif dr == 'cw':
        rmat = list(reversed(mat))
    res = [list(i) for i in zip(*rmat)]
    return res


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            print(matrix[i][j], end=' ')
        print()
print()
otv = rotate(matrix, 'cw')
for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            print(otv[i][j], end=' ')
        print()
