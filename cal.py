print(".........................Calculator..................")

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operator = input("Select the operator (+, -, *, %, /): ")

if operator == "+":
    def add(number1, number2):
        return number1 + number2

    result = add(number1, number2)
    print("The result is:", result)

elif operator == "-":
    def subtract(number1, number2):
        return number1 - number2

    result = subtract(number1, number2)
    print("The result is:", result)

elif operator == "*":
    def multiply(number1, number2):
        return number1 * number2

    result = multiply(number1, number2)
    print("The result is:", result)

elif operator == "%":
    def modulus(number1, number2):
        return number1 % number2

    result = modulus(number1, number2)
    print("The result is:", result)

elif operator == "/":
    def divide(number1, number2):
        return number1 / number2

    result = divide(number1, number2)
    print("The result is:", result)

else:
    print("Incorrect operator! Try again.")