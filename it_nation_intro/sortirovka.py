#massiv = [1, 2, 3, 4, 5]
#new_box =[]
#new_box = sorted(massiv)
#print(new_box)

def is_sorted(box_numbers: list) -> bool:

    new_box = []
    massiv = []
    new_box = box_numbers
    massiv = sorted(new_box) #сортировать массыв повозростанию sort()
    if box_numbers == massiv:
        return True
    else:
        return False
    pass


def get_location(coordinates: list, commands: list) -> list:

    x = int(coordinates[0])
    y = int(coordinates[1])
    for i in range(len(commands)):
        if "forward" in commands[i]:
            y += 1
        if "back" in commands[i]:
            y -= 1
        if "right" in commands[i]:
            x += 1
        if "left" in commands[i]:
            x -= 1
    return [x, y]
    pass


import math


def get_plan(current_production: int, month: int, percent: int):

    new_plan = []
    for i in range(1, month + 1):
        current_production = current_production +current_production *      percent / 100
        current_production = math.floor(current_production)
        new_plan.append(current_production)
    return new_plan
    pass


from math import floor


def get_speed_statistic(test_results: list) -> list:

    new_statistic = []
    if test_results == []:
        new_stat = [0, 0, 0]
        return new_stat
    else:
        resalt_nim = min(test_results)
        new_statistic.append(resalt_nim)
        resalt_max = max(test_results)
        new_statistic.append(resalt_max)
        resalt_sr = sum(test_results) / len(test_results)
        resalt_sredinie = floor(resalt_sr)
        new_statistic.append(resalt_sredinie)
        return new_statistic
    pass
