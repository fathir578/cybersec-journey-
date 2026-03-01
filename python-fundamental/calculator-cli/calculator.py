name = ""

while name == "":
    name = input("enter your name: ").strip()
    if not name :
        print("please enter your name before!!")

def welcome():
    style = "*" * (len(name)+6)
    print (style)
    print (f"** {name} ** ")
    print (style)

welcome()

number1 = int(input("Enter first number: "))
opr = input("Enter operator: +, -, *, /: ")
number2 = int(input("Enter second number: "))

if opr == "+":
    print (number1 + number2)
elif opr == "-":
    print (number1 - number2)
elif opr == "*":
    print (number1 * number2)
elif opr == "/":
    while True:
        number2 = int(input("enter second number not (0): "))
    
        if number2 != 0 :
            print(number1 / number1)
            break
        else:
            print ("ERROR : Division by zero,are you dumb?, please retry")
    