def cap_1(func):
    def wrapper():
        original_text = func()
        mod1 = original_text.split(' ')
        mod2 = []
        mod3 = []
        mod4 = []
        for w in mod1:
            mod2.append(w.lower())
        for w in mod2:
            mod3.append(list(w))
        for w in mod3:
            w[0] = w[0].upper()
        for w in mod3:
            mod4.append(''.join(w))
        mod_text = ' '.join(mod4)
        return mod_text
    return wrapper
@cap_1
def in_text():
    text = input('Введите текст:')
    return text
print(in_text())
