import itertools
#lst = [9, 101, 8]
#lst = [8, 71, 7, 72]
#lst = [1, 0, 0]
lst = [222, 33, 10]
spper = list(itertools.permutations(lst))
#print(spper)
spj = []
for i in spper:
    st = ''.join(map(str, i))
    spj.append(int(st))
#print(spj)
sbch = max(spj)
print(f'Самое большое число: {sbch}')














# d = {}
# a = []
# s = list(map(str, lst))
# print(s)
# for i in s:
#     for j in range(len(i)):
#         a.append(i[j])
#         print(a)
#         b = s.count(i)
#         d[i] = a, b
#     a = []
# print(d)
# dsor = dict(sorted(sorted(d.items(), key=lambda x: x[1][0]), reverse=True))
# print(dsor)
# b = list(dsor.keys())
# print(b)
# c = []
# for i in b:
#     c.append(i * dsor[i][1])
# print(c)
# sbch = ''.join(c)
# print(sbch)