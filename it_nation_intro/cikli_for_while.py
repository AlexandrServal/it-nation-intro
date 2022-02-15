def print_numbers(n: int) -> None:

    for n in range(0, n, 1):
        print(n)
    pass

m = 5
sum = 0
for i in range(1, m + 1):
    sum += i
print(sum) # 15

def get_drinks(number_of_guests: int) -> int:

    sum = 0
    for i in range(1, number_of_guests + 1):
        sum += i
    return sum
    pass

def get_drinks_with_step(number_of_guests: int, step: int) -> int:

    sum = 0
    for i in range(1, number_of_guests + 1, step):
        sum += i
    return sum
    pass

def calculate_profit(amount: int, percent: float, period: int) -> float:

    a = amount
    for i in range(1, period + 1):
        amount =amount + amount * percent / 100
    amount = amount - a
    return amount
    pass
