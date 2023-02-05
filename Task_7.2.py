def code(str, n):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    ABC = abc.upper()
    diccod = {}
    rez = ''
    str = vvod
    #n =int(input())
    for i in range(len(abc)):
        diccod[abc[i]] = abc[i - len(abc) + n]
        diccod[ABC[i]] = ABC[i - len(ABC) + n]
    for i in str:
        rez += (diccod.get(i, i))
    return rez
n = int(input('Введите сдвиг:'))
vvod = input('Введите строку:')
print(code(str, n))
