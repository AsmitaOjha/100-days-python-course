# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
print("Welcome to Python Pizza Deliveries !\n")
size=input("What size pizza do you want? S, M, or L : ")
if(size=='S'):
    price = 15
elif(size=='M'):
    price = 20
elif(size=='L'):
    price = 25
pepperoni = input("Do you want pepperoni ? Y or N :")
if(size =='S'):
    if(pepperoni=='Y'):
        price +=2
else:
    if(pepperoni=='Y'):
        price +=3
extra_cheese = input("Do you want extra cheese ? Y or N :")
if(extra_cheese=='Y'):
    price +=1
else:
    print("Not in our menu:)")
print(f"Your bill is : ${price}")
#assignment code
# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# bill = 0

# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3
    
# if extra_cheese == "Y":
#   bill += 1
  
# print(f"Your final bill is: ${bill}.")
