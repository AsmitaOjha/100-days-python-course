print("Don't change the code below 🙃")
row1 = ['💙', '💙', '💙']
row2 = ['💙', '💙', '💙']
row3 = ['💙', '💙', '💙']
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? \t")
print("Don't change the code above 👆")
#write your code below this row 
horizontal = int(position[0])
vertical = int(position[1])
#map[vertical -1][horizontal -1] = "X"
selected_row = map[vertical - 1]
selected_row[horizontal -1] = "X"
print("Don't change the code below ")
print(f"{row1}\n{row2}\n{row3}")