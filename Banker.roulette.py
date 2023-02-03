import random
#Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
#⬆️ Don't change the code above👆
num = len(names)
pay_bill = random.randint(0,num-1)
person_who_will_pay = names[pay_bill]
print(person_who_will_pay + " is going to pay everybody's food bill")