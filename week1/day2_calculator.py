num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
if num2 != 0:
    print(f"Division: {num1 / num2}")
else:
    print("Cannot divide by zero.")

temperature = float(input("Enter temperature in Celsius: "))
fahrenheit = temperature * 9 / 5 + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")