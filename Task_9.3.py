#import collections
sl = {}
with open('Task_9.txt', 'r', encoding= 'utf-8') as tekst:
    a = tekst.read().lower()
    #sl = dict(collections.Counter(a))
    for i in a:
        sl[i] = sl.get(i, 0) +1
    sorsl = sorted(sl.items(), key=lambda x: (-x[1], x[0]))
#print(a)
#print(sl)
for i in range(10):
    print(f'{sorsl[i][0]}-{sorsl[i][1]}')







