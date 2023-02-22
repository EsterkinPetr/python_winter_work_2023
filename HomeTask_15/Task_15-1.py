res = []
def fu_key(dct, x):
    for key in dct.keys():
        if type(dct[key]) == dict:
            if key == x:
                res.append(dct[key])
            fu_key(dct[key], x)
        else:
            if key == x:
                res.append(dct[key])
    return res
d = {1: 1, 2: 2, 3: {2: 22, 3: {1: 111, 2: 222, 3: {0: 1111, 1: 2222, 2: 3333}}, 1: 11, 6: 22}}
x = int(input())
print(fu_key(d, x))









