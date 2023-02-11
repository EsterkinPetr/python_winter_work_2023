import calendar
import datetime
import locale
y = 2023
spfd = []
for month in range(1, 13):
    cou = 0
    for cm in range(1, calendar.monthrange(y, month)[1] +1):
        if calendar.weekday(y, month, cm) == 3:
            cou += 1
            if cou ==3:
                spfd.append((y, month, cm))
                continue
print(spfd)
locale.setlocale(locale.LC_ALL, 'ru')
for day in spfd:
    print((datetime.date(day[0], day[1], day[2]).strftime('%d.%m.%Y')))






