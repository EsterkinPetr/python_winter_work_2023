def sortir(lst):
    count = -1
    while count != 0:
        count = 0
        for i in range(len(lst)-1):
            if lst[i] > lst[i + 1]:
                a, b =lst[i], lst[i + 1]
                lst[i], lst[i + 1] = b, a
                count += 1
            else:
                continue
    return lst
s = list(range(12, 0, -1))
print(s)
print(sortir(s))
