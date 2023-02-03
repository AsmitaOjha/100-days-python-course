#BMI body mass index
#BMI = weight(kg)/(height^2)
height = input("Enter your height in metres ")  #eg. 1.45 which is the height of a person in metre
weight = input("Enter your weight in kilogram ")  #eg. 56 which is the weight of person in kilogram
BMI = float(weight)/float(height)**2
print("The BMI is : ")
print(int(BMI))
