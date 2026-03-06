from time import sleep

name = ""
while name == "":
    name = input("enter your name: ").strip()
    if not name :
        print("please enter your name before!!")
def exit_program():
    print('program akan di hentikan')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    print('program dihentikan')
    exit()

def welcome():
    style = "*" * (len(name)+6)
    print (style)
    print (f"** {name} ** ")
    print (style)


welcome()

def calculate(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b    
    else:
        raise ValueError("Invalid operator. Please use +, -, *, or /.")

def inpurt_number():
    while True:
        try:
            number1 = int(input('Enter frist number: '))
            opt = input('Enter operator(+, *. -. /): ')
            number2 = int(input('Enter second number: '))

            result = calculate(number1, opt, number2)
            print('hasil: ', result)
            break

        except ValueError as e:
            print('Error ;', e)
        except ZeroDivisionError as e:
            print('Error: ', e)
inpurt_number()

while True:
    pertanyaan = input('apakah anda ingin menghitung lagi? (y/n): ')
    if pertanyaan.lower() == 'y':
        inpurt_number()
    else:    
        exit_program()