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
a2 = maks - a
b2 = maks -b
c2 = maks - c
d2 = maks -d
e2 = maks - e
if a ==maks :
    if b2 < c2 :
        otv = b
    else :
        otv = c
    if c2 < otv :
        otv = c
    if d2 < otv :
        otv = d
    if e2 < otv :
        otv = e
if b == maks :
    if a2 < c2 :
        otv = a
    else :
        otv = c
    if c2 < otv :
        otv = c
    if d2 < otv :
        otv = d
    if e2 < otv :
        otv = e
if c == maks :
    if a2 < b2:
        otv = a
    else:
        otv = b
    if d2 < otv:
        otv = d
    if e2 < otv:
        otv = e
if d == maks :
    if a2 < b2:
        otv = a
    else:
        otv = b
    if c2 < otv:
        otv = c
    if e2 < otv:
        otv = e
if e == maks :
    if a2 < b2:
        otv = a
    else:
        otv = b
    if c2 < otv:
        otv = c
    if d2 < otv:
        otv = d
print(otv)












