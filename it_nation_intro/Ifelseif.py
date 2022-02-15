def can_buy_beer(age: int) -> str:

    if  age >= 18:
        print("You can buy beer")
    else:
        print("You can not buy beer")
    pass
# def can_buy_beer(age: int) -> str:
  #  # write your code here
   # if  age >= 18:
       # ("You can buy beer")
   # else:
    #    print("You can not buy beer")
   # pass
def get_tips_rating(amount: int) -> str:

    if amount == 0:
        return "terrible"
    elif amount <= 10:
        return "poor"
    elif amount <= 20:
        return "good"
    elif amount <= 50:
        return "great"
    else:
        return "excellent"
pass

def calculate_taxes(income: int) -> float:

    if income <= 1000:
        return income * 0.02
    elif income <= 10000:
        return income * 0.03
    else:
        return income * 0.05
    pass
