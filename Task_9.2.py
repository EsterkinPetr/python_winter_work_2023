gl = ['а','у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
w0 = input()
ingl = []
for i in range(len(w0)):
    if w0[i] in gl:
        ingl.append(i)
#print(ingl)
n =int(input())
i = 1
di = {}
diin = {}
si =[]
while i <= n:
    di[i] = input()
    i += 1
for w in di.values():
    for i in range(len(w)):
        if w[i] in gl:
            si.append(i)
    diin[w] = si
    si = []
like = []
for key in diin :
    if diin[key] == ingl:
        like.append(key)
#print(di)
#print(diin)
#print(like)
print(' ,'.join(like))

