n =int(input())
d = []
for i in range(1, n + 1):
    if n % i == 0:
        d.append(i)
print(*d, sep=" ")
