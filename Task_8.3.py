issp = ['abab', 'xx', 'aaaaaaa', 'abcbab']
spkor = []
for i in range(len(issp)):
    spkor.append((set(issp[i]), issp[i]))
#print(spkor)
sspkor = sorted(spkor, key=lambda x: (-len(x[0]), x[1]))
sprez = []
for i in sspkor:
    sprez.append(i[1])
print(sprez)

