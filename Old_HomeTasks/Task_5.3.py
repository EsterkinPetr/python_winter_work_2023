n = int(input())
rf = [1, 1]
for i in range(2, n):
    rf.append((rf[i - 1] + rf[i - 2]))
print(*rf, sep=' ')
