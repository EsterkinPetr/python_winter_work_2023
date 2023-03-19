def fu(s):
    sp = list(s)
    print(sp)
    if len(sp) % 2 == 0:
        for i in range(int(len(sp) / 2)):
            if sp[0] == '(':
                sp.remove('(')
                try:
                    sp.remove(')')
                except ValueError:
                    res = False
                    break
                else:
                    print(sp)
                    continue
            else:
                res = False
                break
        if not sp:
            res = True
    else:
        res = False
    return res

#st = ')'
#st = ')(()))'
st = '(())((()())())'
#st = '('
#st = '(()()('
#st = ')('
print(fu(st))
