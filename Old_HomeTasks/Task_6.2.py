sk1 = input().split(', ')
sk2 = input().split(', ')
tes1 = set(sk1)
tes2 = set(sk2)
oba = tes1 & tes2
otv = len(oba)
print(f'Ответ:{otv}')
