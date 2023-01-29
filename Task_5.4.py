n = int(input())
if n != 1:
    s = {}
    q = n // 2
    zn = 0
    i = 0
    for k in range (q):
        l = n - 1 - k
        for j in range (k, l):
            zn +=1
            s[i, j] = zn
        j = j + 1
        for i in range(k,l):
            zn +=1
            s[i, j] = zn
        i= i + 1
        for j in range (l, k, -1):
            zn +=1
            s[i, j] = zn
        j = j - 1
        for i in range (l, k, -1):
            zn +=1
            s[i, j] = zn
    if n % 2 != 0:
        j = j +1
        zn +=1
        s[i, j] = zn
    for i in range (n):
        for j in range(n):
            if s[i, j] < 10:
                print((f' {s[i, j]} '), end = '')
            else:
                print(s[i, j],'',end ='')
        print()
else:
    print(n)