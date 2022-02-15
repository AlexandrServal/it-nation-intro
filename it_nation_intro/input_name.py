#name = input("What's your name?:  ")
#massage = f"Happy birthday, {name}!"
#print(massage)
# "Happy birthday, {name}!"

# input_ int
age = int(input("What number do you want to check?"))
#print(type(age))
new_age = age / 2
new_age2 = age // 2
if new_age == new_age2:
    print("Even")
else:
    print("Odd")