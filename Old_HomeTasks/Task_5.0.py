sl = input()#Ввели слово
ssl = list(sl)#преобразовали слово в список
gl = ['a', 'e', 'i', 'o','u']
sg = []#список гл. слова
ss = []#список согл. слова
res = []
for i in range (len(ssl)):
    if ssl[i] in gl:
        sg.append(ssl[i])
    else:
        ss.append(ssl[i])
#print(ss, sg)
if abs(len(ss) - len(sg)) <= 1:#проверяем условие,что длина списка гласных и согласных отличается не более чем на 1 или равны
    if len(ss) > len(sg):
        for i in range(len(sg)):
            res.append(ss[i])
            res.append(sg[i])
        res.append(ss[len(ss) - 1])
    elif len(ss) == len(sg):
        for i in range(len(sg)):
            res.append(ss[i])
            res.append(sg[i])
    else:
        for i in range(len(ss)):
            res.append(sg[i])
            res.append(ss[i])
        res.append(sg[len(sg) - 1])
    print(''.join(res))
else:
    print('imposible')