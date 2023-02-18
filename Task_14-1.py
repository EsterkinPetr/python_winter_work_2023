def diq(n):
    if n < 10:
        return 1
    else:
        return 1 + diq(n // 10)
print(diq(int(input())))
