sp = list(map(int, input().split()))
sp =sorted(sp)
ok = 1
x = 0
for i in sp:
    ok = ok * i
for i in range(max(sp),ok + 1):
    for j in sp:
        if i % j == 0:
            nok = i
            x += 1
        else:
            x = 0
            break
    if x == len(sp):
        break
    continue
print(i)
