x = "Hello" # превратить строку в массив
x = list(x)
print(x)
a = len(x)
print(a)
massiv = []
if a / 2 == a // 2:
    for i in range(1, len(x), 2):
        b = x[i]
        c = x[i-1]
        d = c + b
        massiv.append(d)
else:
    for i in range(1, len(x), 2):
        b = x[i]
        c = x[i-1]
        d = c + b
        massiv.append(d)
    e = x[-1] + "_"
    massiv.append(e)
print(massiv)

'''
    x = list(string)
    long_list = len(x)
    massiv = []
    if long_list / 2 == long_list // 2:
        for i in range(1, len(x), 2):
            b = x[i]
            c = x[i-1]
            d = c + b
            massiv.append(d)
    else:
        for i in range(1, len(x), 2):
            b = x[i]
            c = x[i-1]
            d = c + b
            massiv.append(d)
        e = x[-1] + "_"
        massiv.append(e)
    print(massiv)
'''