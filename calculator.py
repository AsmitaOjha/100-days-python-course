print("This is simple calculator")
first = input("Enter first number: ")
second = input("Enter second number: ")
operator = input("Enter the operator (+, -, *, /, %): ")
first = int(first)
second = int(second)
if operator == '+':
    print(first + second)
elif operator == '-':
    print(first - second)
elif operator == '*':
    print(first * second)
elif operator == '/':
    print(first / second)
elif operator == '%':
   print(first % second)
else:
    print("Invalid operator")
