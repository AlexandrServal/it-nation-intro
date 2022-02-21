ls = []
print(ls)
massiv = sorted(ls)
print(massiv)
print(len(ls))
'''
def get_unique_items(ls: list) -> list:
    # write code here
    massiv = sorted(ls)
    chislo = massiv[0]
    massiv1 = []
    massiv1.append(chislo)
    for i in range(1, len(massiv)):
        if massiv[i] != massiv[i - 1]:
            a = massiv[i]
            massiv1.append(a)
    return massiv1
    pass
'''