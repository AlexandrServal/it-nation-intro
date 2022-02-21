def sum_list_items(ls: list) -> int:
    a = 0
    i = 0
    if len(ls) == 0:
        return 0
    elif len(ls) >= 1:
        for i in range(0, len(ls)):
            a += ls[i]
        return a
    pass
