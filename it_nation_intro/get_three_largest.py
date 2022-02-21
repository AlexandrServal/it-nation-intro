def get_three_largest(ls: list) -> list:
    massiv = []
    massiv1 = []
    if len(ls) == 0:
        return ls
    elif len(ls) <= 3:
        return ls
    elif len(ls) > 3:
        massiv = sorted(ls)
        massiv1.append(massiv[-1])
        massiv1.append(massiv[-2])
        massiv1.append(massiv[-3])
        return massiv1
    pass
