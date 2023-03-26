def roma_dec(roma):
    dec = 0
    slroma = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
              'V': 5, 'IV': 4, 'I': 1}
    while len(roma) != 0:
        for k in slroma:
            if roma.startswith(k):
                dec += slroma[k]
                roma = roma[len(k):]
    return dec
while True:
    roma = input()
    if roma != '0':
        print(f'{roma} ={roma_dec(roma)}')
    else:
        break




