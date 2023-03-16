import keyword

spks = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
rezsp = []
stekst ='В случае программирования интроспекция означает возможность изучать break что-либо, чтобы from определить, что это  while такое, что оно умеет и что может делать.Python keywords are special reserved words that have specific class meanings and purposes and can’t be used for anything but those specific purposes. '
sptekst = stekst.split()
for word in sptekst:
    if word in (spks):
        rezsp.append('<kw>')
    else:
        rezsp.append(word)
print(rezsp)
print(' '.join(rezsp))



