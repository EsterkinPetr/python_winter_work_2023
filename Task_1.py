x = int(input())
y = int(input())
a = x +y
b = x - y
c = x * y
d = x /y
e = x // y
if a > b :
    maks = a
else:
    maks = b
if c > maks :
    maks = c
if d > maks :
        maks = d
if e > maks :
            maks = e
print(maks)