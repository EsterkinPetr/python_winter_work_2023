import re
instr = '-1 0 1 2f 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 33 44 45 46  123  444 4444 4546 045 01 -45'
vvod = int(input('ведите двузначное число: '))
des = vvod // 10
ed = vvod % 10

#print(re.findall(fr'([1-{des}][0-{ed}])', instr))

print(*re.findall(fr'(?:(?<![-\d])\d(?!\d)|(?<![-\d])[1-{des}][0-{ed}](?!\d))', instr))


