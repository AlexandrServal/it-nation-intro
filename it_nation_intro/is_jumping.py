number = 23454
massiv = []
# странный цикл
while number > 0:
    massiv.append(number % 10)
    number //= 10
    print(number)
massiv.reverse()
print(massiv)  # [1, 2, 3, 4]
# перобразование числа в массив
a = "JUMPING"
i = 1
for i in range(1, len(massiv)):
    b = abs(massiv[i]-massiv[i-1])
    print(b)
    if b == 1: #massiv[i]-massiv[i-1] == 1 or massiv[i]-massiv[i-1] == -1:
        a = "JUMPING"
    elif b > 1:      # massiv[i] - massiv[i - 1] > 1:
        a = "NOT JUMPING"
    break
print(a)

'''
def is_jumping(number: int) -> str:
    # write your code here
    massiv = []
    while number > 0:
        massiv.append(number % 10)
        number //= 10
    massiv.reverse()
    a = "JUMPING"
    i = 1
    for i in range(1, len(massiv)):
        b = abs(massiv[i]-massiv[i-1])
        #c = massiv[i]-massiv[i-1]
        if b == 1: 
            a = "JUMPING"
        else:      
            a = "NOT JUMPING"
            break
    return a
    pass
'''