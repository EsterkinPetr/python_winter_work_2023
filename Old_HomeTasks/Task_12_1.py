def fu(lst):
    smi = [i for i in range(len(lst)) if lst[i] == min(lst)]
    sma = [i for i in range(len(lst)) if lst[i] == max(lst)]
    return smi, sma
x = [1, 2, 3, 4, 1, 2, 3, 4, 1, 4]
print(fu(x))
