pr1 = input()
pr2 = input()
pr1 = pr1.lower()
pr2 = pr2.lower()
dict1 = {}
dict2 = {}
for i in pr1:
    if (str(i)).isalpha():
        if i not in dict1:
            dict1[i] = 0
        dict1[i] += 1
for i in pr2:
    if (str(i)).isalpha():
        if i not in dict2:
            dict2[i] = 0
        dict2[i] += 1
if dict1 == dict2:
    print('True')
else:
    print('False')