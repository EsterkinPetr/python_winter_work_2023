def tri_2(n):
    print('*' * n)
    if n > 1:
        tri_2(n - 1)
        print('*' * n)
tri_2(int(input()))
