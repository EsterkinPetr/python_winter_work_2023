
pr = input()#предложение поданное наввод(строка)
sppr = list(pr.split(' '))#преобразоали строку в список с разделителем пробел
dl = []#создали пустой список, куда будем записывать длины слов
for sl in sppr :#для каждого слова в списке записали в список dl его длину
    dl.append(len(sl))
maxdl = max(dl)#нашли максималььную длину слова
for sl in sppr:#проверяем все слова в списке, когда длина слова равна макс. длине- печатаем слово
    if len(sl) == maxdl:
        print(sl)
