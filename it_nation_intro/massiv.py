def make_stickers(details_count: int, robot_part: str) -> list:

    add = []
    for i in range(1, details_count + 1):
        detail = f"{robot_part} detail #{i}"
        add.append(detail)
    return add
    pass


def double_power(current_powers: list) -> list:
    massiv = []
    for i in current_powers:
        a = (i)
        b = a * 2
        massiv.append(b)
    return massiv
    pass



def is_sorted(box_numbers: list) -> bool:

    for i in range(len(box_numbers)):
        if (i) <= (i - 1):
            return True
    pass
