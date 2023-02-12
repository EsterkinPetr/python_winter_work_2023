def ar_rom(ar):
    slroma = {900: 'CM', 500: 'D', 400: 'CD', 90: 'XC', 50: 'L', 40: 'XL', 9: 'IX',
              5: 'V', 4: 'IV'}
    rom = ''
    t = ar//1000
    if t != 0:
        rom += 'M' * t
    h = (ar % 1000) // 100
    if (h * 100) in slroma.keys():
        rom += slroma[h * 100]
    elif (h * 100) > 500:
        rom += 'D' + 'I' * (h - 5)
    else:
        rom += 'C' * h
    d = (ar % 100)//10
    print(d)
    if (d * 10) in slroma.keys():
        rom += slroma[d * 10]
    elif (d * 10) > 50:
        rom += 'L' + 'X' * (d - 5)
    else:

        rom += 'X' * d
    e = ar % 10
    if e in slroma.keys():
        rom += slroma[e]
    elif e > 5:
        rom += 'V' + 'I' * (e - 5)
    else:
        rom += 'I' * e
    return rom
dec = int(input())
print(f'{dec} = {ar_rom(dec)}')








