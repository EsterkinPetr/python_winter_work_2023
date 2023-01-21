lst = [int(i) for i in input().split()]
minel = lst[0]
for el in lst:
    if el < minel:
        minel = el
print(minel)



