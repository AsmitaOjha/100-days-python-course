print(''' 
                                    .---.
                                    |[X]|
                             _.==._.""""".___n__
                            d __ ___.-''-. _____b
                            |[__]  /."""".\ _   |
                            |     // /""\ \\_)  |
                            |     \\ \__/ //    |
                            |pentax\`.__.'/     |
                            \=======`-..-'======/
                             `-----------------'   hjw
''')
print("\t Welcome to game to find the jackpot")
print("You are a mission to find hidden jackpot, collect it and take pics of strange this you encounter in the journery\n")
choice1 = input('You are standing in a place. There are two choices to go out either you have to go through "ladder" or choose "lift"\n').lower()
if choice1 == "ladder":
  choice2 =input('You arrived where there are ways to go namely: "A", "B", "C", click a picture.\n').upper()
  if choice2 =="A":
    print("You are infront of tiger. GAme over") 
  elif choice2 == "B":
    print("You are again in the place where you started. So you are lost. Game over.")
  elif choice2 == "C":
    choice3=input("You are on bank of river. Click a picture. Now to you are seeing a temple across the river.To reach thier you have two choices: either 'wait' for the boat or wear the swimming suit and 'swim' \n").lower()
    if choice3 == 'wait':
      print("You reached the temple and found the jackpot.Click the pic. Hurry!!!You won the game. ")
    else:
      print("You are surrounded by corcodiles. You lost. GAme over.")
    
  else:
    print("GAme over")
else:
  print("You are in top of roof. You lose. GAme over.")

  