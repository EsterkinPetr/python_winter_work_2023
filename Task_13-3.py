lst = [1, 2, 3, 44, 56, 13, 47, 99, 123, 14]
def ne_ch(x):
    for i in x:
        if i % 2 == 1:
            yield i
gen = ne_ch(lst)
for i in gen:
    print(i, end=' ')



