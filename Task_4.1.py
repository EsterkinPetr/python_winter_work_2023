vvod = input().split()
if vvod[1] == '+':
    print(float(vvod[0]) + float(vvod[2]))
elif vvod[1] == '-':
    print(float(vvod[0]) - float(vvod[2]))
elif vvod[1] == '*':
    print(float(vvod[0]) * float(vvod[2]))
elif vvod[1] == '/':
    if float(vvod[2]) == 0:
        print('Делить на ноль нельзя!')
    else:
        print(float(vvod[0]) / float(vvod[2]))