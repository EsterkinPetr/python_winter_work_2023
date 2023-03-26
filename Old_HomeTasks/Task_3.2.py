ch = input()
s =[]
for i in range(10):
    s.append(ch.count(str(i)))
for k, v in enumerate(s):
    print(f'{k}-{v}')


