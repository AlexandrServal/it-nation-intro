amount = 18
cookiePrice = 8
candyPrice = 7
# rest = amount - cookiePrice
amount = amount - cookiePrice
has_enough_money = True
# print("Amount is", amount)
print("has enough money", has_enough_money)
# if amount >= candyPrice:
if has_enough_money:
    print("I have enough money")
else:
    print("I do not have enough money")