itogo = 0
n = 0
while True:
    zp = int(input())
    if zp != 0 :
        itogo += zp
        n += 1
    else:
        n +=1
        break
print(itogo / n)

