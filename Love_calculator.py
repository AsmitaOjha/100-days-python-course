<<<<<<< HEAD
print('Welcome to the Love Calculator !')
name=input("What is your name? : ").lower()
their_name=input("What is their name? : ").lower()
print(name)
print(their_name)
X = name.count("t") + their_name.count("t") + name.count("r") + their_name.count("r") + name.count("u") +name.count("e") + their_name.count("u") + their_name.count("e")
Y = name.count("l") + their_name.count("l") + name.count("o") + their_name.count("o") + name.count("v") +name.count("e") + their_name.count("v") + their_name.count("e")
Love_score = int(str(X)+str(Y))

print(Love_score)
if(Love_score<10 or Love_score>90):
    print(f"Your score is {Love_score}, you go together like coke and mentos.")
elif(Love_score>=40 and Love_score<=50):
    print(f"Your score is {Love_score},you are alright together.")
else:
    print(f"Your score is {Love_score}")

# print(f"Love percentage : {str(X)}{str(Y)} %")
# print(f"Love percentage: {X}{Y}%")

=======
print('Welcome to the Love Calculator !')
name=input("What is your name? : ").lower()
their_name=input("What is their name? : ").lower()
print(name)
print(their_name)
X = name.count("t") + their_name.count("t") + name.count("r") + their_name.count("r") + name.count("u") +name.count("e") + their_name.count("u") + their_name.count("e")
Y = name.count("l") + their_name.count("l") + name.count("o") + their_name.count("o") + name.count("v") +name.count("e") + their_name.count("v") + their_name.count("e")
Love_score = int(str(X)+str(Y))

print(Love_score)
if(Love_score<10 or Love_score>90):
    print(f"Your score is {Love_score}, you go together like coke and mentos.")
elif(Love_score>=40 and Love_score<=50):
    print(f"Your score is {Love_score},you are alright together.")
else:
    print(f"Your score is {Love_score}")

# print(f"Love percentage : {str(X)}{str(Y)} %")
# print(f"Love percentage: {X}{Y}%")

>>>>>>> a141d86836fa82dc66c0193533077da0c2cf6fcd
