import re
def tel_nr(st):
    res = re.findall(r'\+7\((?:812|921)\)\d{3}-\d{2}-?\d{2}', st)
    return res
a = '5+7(921)934-11-29ffff+7(812)234-4545'
print(*tel_nr(a))
