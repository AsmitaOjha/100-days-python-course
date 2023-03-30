student_scores = input("Input a list of student scores").split()
for n in range(0, len(student_scores)):
 student_scores[n]= int(student_scores[n])
print(student_scores)
#don't change the code above
#write your code below this row
highest_score=0
for scores in student_scores:
 if(highest_score<scores):
  highest_score=scores
print(f"The highest score is the class is: {highest_score}")


  