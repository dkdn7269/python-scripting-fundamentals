expression = (input("Expression: ")) # get the full expression as a string e.g. '1 + 1'

x, y, z = expression.split(" ") # split at spaces — x = first number, y = operator, z = second number

x = float(x)    # convert first number from string to float for math
z = float(z)    # convert second number from string to float — y stays as a string for the if checks

if y == "+":
    interpreter = x + z
elif y == "-":
    interpreter = x - z
elif y == "*":
    interpreter = x * z
elif y == "/":
    interpreter = x / z

print(f"{interpreter:.1f}") # print result formatted to exactly one decimal place
