expression = (input("Expression: "))

x, y, z = expression.split(" ")

x = float(x)
z = float(z)

if y == "+":
    interpreter = x + z
elif y == "-":
    interpreter = x - z
elif y == "*":
    interpreter = x * z
elif y == "/":
    interpreter = x / z

print(f"{interpreter:.1f}")
