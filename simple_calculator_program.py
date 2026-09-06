# calculator program
calculation = input("enter your operator please:  ")
num1 = int(input("enter your first number:  "))
num2 = int(input("enter your second number:  "))


# conditions
if calculation == "+":
    print(f"Your SUM is: {num1 + num2}")
elif calculation == "-":
    print(f"Your SUBTRACTION is: {num1 - num2}")
elif calculation == "*":
    print(f"Your MULITIPLICATION is: {num1 * num2}")
elif calculation == "/":
    print(f"Your DEVISION is: {num1 / num2:.2f}")
else:
    print("we don’t have this operator yet")
