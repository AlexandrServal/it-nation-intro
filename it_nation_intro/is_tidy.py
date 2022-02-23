number = 123445
massiv = []
while number > 0:
    massiv.append(number % 10)
    number //= 10
massiv.reverse()
a = True
i = 1
for i in range(1, len(massiv)):
    if massiv[i] >= massiv[i-1]:
        a = True
    elif massiv[i] < massiv[i-1]:
        a = False
        break
print(a)


'''
def is_tidy(number: int) -> bool:
    # write your code here
    massiv = []
    while number > 0:
        massiv.append(number % 10)
        number //= 10
    massiv.reverse()
    a = True
    i =1
    for i in range(1, len(massiv)):
        if massiv[i] >= massiv[i-1]:
            a = True
        elif massiv[i] < massiv[i-1]:
            a = False
            break
    return a
    pass
'''