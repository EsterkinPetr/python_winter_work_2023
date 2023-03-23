def func(s1, s2):
    count = 0
    if len(s1) - len(s2) == 0:
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            else:
                count += 1
                print(count)
                if count > 1:
                    res = False
                    break
        res = True
    elif len(s1) - len(s2) == 1:
        if s2 in s1:
            res = True
        else:
            res = False
    elif len(s1) - len(s2) == -1:
        if s1 in s2:
            res = True
        else:
            res = False
    else:
        res = False
    return res

a = 'a'
b = ''

print(func(a, b))




