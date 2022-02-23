stringa = "robot"
stringa = stringa.upper() # верхний регистр
massiv = list(stringa) # перевод строки в массив
massiv1 = list(stringa)
new_massiv =[]
new_massiv.append(stringa) # заполнение массива
massiv2 = massiv1
for i in massiv:
    a = i
    massiv1.remove(a) # удалить елемент из массива
    massiv1.append(a) # вставит елемент в массив
    stringa1 = ''.join(map(str, massiv1)) # вставляет переменню вмассив
    new_massiv.append(stringa1)
new_massiv1 = new_massiv.pop(-1)
print(new_massiv)