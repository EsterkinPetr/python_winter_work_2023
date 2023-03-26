s, z = input().split()
sls = {}
slz = {}
for i in s:
    if i not in sls:
        sls[i] = 0
    sls[i] += 1
for j in z:
    if j not in slz:
        slz [j] = 0
    slz[j] += 1
if sls == slz:
     print('True')
else:
    print('False')