#sp = ['x', 'y', ['z']]
#sp = [1, 2, 3]
#sp = []
#sp = [1, 2, [3, 4, [5, ]]]
#sp = [1, 2, 3, [4, 5, [6, 7]]]
sp = [[1], [2], []]
res = []


def loa(s):
    for i in s:
        if type(i) == list:
            res.append('spi')
            loa(i)
        else:
            res.append(i)

    return len(res)


print(loa(sp))




