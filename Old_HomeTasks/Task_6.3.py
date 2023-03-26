vvod = input()
let = set()
dig = set()
oth = set()
for i in range(len(vvod)):
    if vvod[i].isalpha():
        let.add(vvod[i])
    elif vvod[i].isdigit():
        dig.add(vvod[i])
    else:
        oth.add(vvod[i])
print(*let)
print(*dig)
print(*oth)
