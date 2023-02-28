def deco(fu):
    def wraper(*args, **kwargs):
        lta = []
        for x in args:
            xstr = str(x)
            for el in xstr:
                if el.isalpha():
                    lta.append(el.upper())
        value = fu(*args, **kwargs)
        return lta
    return wraper
@deco
def fu(*args, **kwargs):
    return "Готово!"
print(fu('asdfg', 5, a = 2))





