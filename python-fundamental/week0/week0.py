name = str(input("What is your name? "))

def print_name_with_border(name):
    name = name.strip().upper()
    width = len(name) + 4
    border = "*" * width
    print(border)
    print(f"* {name} *")
    print(border)

print_name_with_border(name)



# print("Hello, ", end="")
# print(name)
# print("hello", name, sep="---", end="!!!\n")

# print('.', end="")

number = int(input("Enter a number: "))

for i in range(number):
    print(i+1, end="")

user = ['andi', 'budi', 'caca','andi', 'budi', 'caca', 'andi', 'budi', 'caca','andi', 'budi', 'caca','andi', 'budi', 'caca','andi', 'budi', 'caca']

print(f'\n'.join(user))