#Write your code below this row 👇
total=0
for number in range(2,101,2):
 #print(number)
 total +=number
print(total)
#odd sum 1+3+5+...+99 = ?
# odd_sum=0
# for number in range(1,100,2):
#  print(number)
#  odd_sum=number+odd_sum
# print(odd_sum)
#alternative method for sum of even numbers:
total2 =0
for number in range(1,101):
 if number % 2 ==0:
  total2 +=number
print(total2)