import re
def abr(st):
     lstlet = re.findall(r'\b[а-яА-Я]', st)
     abrev = (''.join(lstlet)).upper()
     return(abrev)
a = 'Ленинградское высшее инженерное морское училище '
print(abr(a))




