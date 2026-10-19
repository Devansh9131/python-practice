user_name = input("Please enter your name: ")
print(f"Good morning, {user_name}!")

user_age = int(input("Please enter your age: "))
if user_age < 0:
    print("Please enter a valid age.")
elif user_age < 30:
    remaining_years = 30 - user_age
    print(f"Hello {user_name}, you will be 30 in {remaining_years} years.")
elif user_age == 30:
    print(f"Hello {user_name}, you are already 30 years old.")
else:
    print(f"Hello {user_name}, you are older than 30.")
    
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))
print(f"Result: {num1+num2}")