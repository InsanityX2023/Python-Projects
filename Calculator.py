print(
    "You can write either 'add' to add the numbers, 'subtract' to subtract the second number for the first number, "
    "\n 'multiply' to multiply the numbers and 'divide' to divide the first number by the second number.")
print("Hit the enter key on your keyboard to proceed:")
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = str(input("What operation do you want to perform with the numbers?:"))
output = 0
if c == "add":
    output = a + b
elif c == "subtract":
    output = a - b
elif c == "multiply":
    output = a * b
elif c == "divide":
    output = a/b
print(output)
#MEWING