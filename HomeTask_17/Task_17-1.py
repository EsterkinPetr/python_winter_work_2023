import re
st = ' -22a-10 -9 -8aa -7 aa-6 -5 -4 -3 -2 -1 0 a1 2n 3 4 ;5]6;; 7 08 9 010 12 1410 22 222 200 01000 333'
print(re.findall(r'(?<!\d)[02468](?!\d)|-?[1-9]+[02468]+', st))

