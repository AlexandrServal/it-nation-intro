stringa = "1000000000"
#print(stringa)
chislo = int(stringa)
#print(chislo)
massiv = []
while chislo > 0:
    massiv.append(chislo % 10)
    chislo //= 10
massiv.reverse()
print(massiv)
dlinna_stringi = len(stringa)
#print(dlinna_stringi)
dlinna_massiva = len(massiv)
#print(dlinna_massiva)
i= 0
a = 0
summa = sum(massiv)
print(summa)
result = summa/ dlinna_massiva *100
result = round(result)
print(result)


'''
chislo = int(statistics)
    massiv = []
    while chislo > 0:
        massiv.append(chislo % 10)
        chislo //= 10
    massiv.reverse()
    dlinna_stringi = len(statistics)
    dlinna_massiva = len(massiv)
    summa = sum(massiv)
    if summa == 0:
        result = 0
    elif summa == 1:
        dlinna = dlinna_massiva+1
        result = summa/dlinna*100
        result = round(result)
    elif dlinna_stringi == 9 and massiv[0] == 1:
        result = 10    
    else:
        result = summa/dlinna_massiva*100
        result = round(result)
    return result
'''

