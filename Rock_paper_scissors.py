import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
# print(f"Rock {rock}")
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
# print(f"Paper {paper}")
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# print(f"Scissors {scissors}")
#Write your code below this line 👇
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\t"))
if user_choice >=3 or user_choice<0 :
    print("you typed invalid number, you lose 🙃😓")
else:
    print(game_images[user_choice])
    # if(user_choice == 0):
    #     print(f"Rock {rock}")
    # elif(user_choice == 1):
    #     print(f"Paper {paper}")
    # elif(user_choice == 2):
    #     print(f"Scissors {scissors}")
    # date: 2079/11/18 (March 3rd 2023 AD)
    #computer choice
    computer_choice = random.randint(0,2)
    print(f"computer chose : {computer_choice}")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win !!!!✨🏆")
    elif computer_choice ==0 and user_choice ==2:
        print("You lose 🙃😓 ")
    elif computer_choice > user_choice:
        print("You lose 🙃😓")
    elif computer_choice < user_choice:
        print("You win!!!✨🏆")
    elif computer_choice == user_choice:
        print("It's a draw!!!")