def deco(fu):
    def wraper(*args, **kwargs):
        lta = []
        ta = ''
        for x in args:
            if type(x) == str:
                for el in x:
                     if el.isalpha():
                         el = el.upper()
                         ta += el
                     else:
                         ta += el
                lta.append(ta)
                ta = ''
        for x in kwargs:
            if type(kwargs[x]) == str:
                print(kwargs[x])
                for el in (kwargs[x]):
                    if el.isalpha():
                        el = el.upper()
                        ta += el
                    else:
                        ta += el
                lta.append(ta)
                ta = ''
        value = fu(*args, **kwargs)
        return lta
    return wraper
@deco
def fu(*args, **kwargs):
    return "Готово!"
print(fu('asd5fg','zxc',  2, 5, a = 2,b = 'zyu3gh', c = '2jklb'))






