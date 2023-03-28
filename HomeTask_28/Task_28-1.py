def inv(sp):
    count = 0
    for i in range(len(sp)):
        for j in range(len(sp)):
            if i < j and sp[i] > sp[j]:
                count += 1
                print(f'{count},{i} < {j}, {sp[i]} > {sp[j]}')
    return count


a = [5, 4, 3, 2, 1]
print(inv(a))

