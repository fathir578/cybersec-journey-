x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

z = x + y

print (f"The sum of {x} and {y} is {z}")

data = [1, 2, 3, 4, 5]

for i in data:
    if i % 2 == 0:
        print (f"{i} \nis even")
    else:
        print (f"{i} \nis odd")

print (f"The sum of {data} is {sum(data)}")
