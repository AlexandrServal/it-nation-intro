number = 123456
massiv = []
while number > 0:
    massiv.append(number % 10)
    number //= 10
massiv.reverse()
print(massiv)
sum = 0
for i in range(len(massiv)):
    sum  = massiv[i]
a = sum
print(a)

def is_special_number(number: int) -> str:
    # write your code here
    massiv = []
    while number > 0:
        massiv.append(number % 10)
        number //= 10
    massiv.reverse()
    a= 'Special!!'
    i = 0
    for i in range(0, len(massiv)):
        if massiv[i]<=5:
            a = 'Special!!'
        elif massiv[i]>5:
            a = 'NOT!!'
            break
    return a
    pass
