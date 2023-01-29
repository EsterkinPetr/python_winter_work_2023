n = int(input())
a = [[0 for j in range(n)]for i in range(n)]
for i in range (n):
    a[i][0] = 1
for i in range (1,n):
    for j in range(1,n):
        a[i][j] = a[i -1][j - 1] + a[i - 1][j]
for i in range(n):
    for j in range (n):
        if a[i][j] != 0:
            print(a[i][j],'',end ='')
    print()