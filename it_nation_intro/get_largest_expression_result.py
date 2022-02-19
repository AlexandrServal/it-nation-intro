from math import sqrt

a = 3
b = 4
summa = a + b
raznost = a - b
proizvedenie = a * b
chastnoe = a / b
c = (summa - raznost)/ 2
d = summa - c
print(d, c)
i = sqrt(proizvedenie/chastnoe)
e = proizvedenie/i
print(e, i)

'''
def get_largest_expression_result(a, b):
    
    if a >= 1 and b >= 1:
        c = a * b
        return c
    elif 0 < b < 1 and a >= 1:
        c = a / b
        return c
    elif a <= -1 and b <= -1:
        c = a * b
        return c
    elif a <= -1 and b >= 1:
        c = a + b
        return c
    elif a >= 1 and b <= -1:
        c = a - b
        return c

    pass
'''
