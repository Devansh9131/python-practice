# Part 1: even/odd
num = int(input("Enter your number: "))
if num%2==0:
    print('Number is even.')
else:
    print('Number is odd.')


# Part 2: grade calculator
score = int (input("Enter your score: "))
if score<0 or score>100:
    print('Please enter a valid score between 0 and 100.')
elif score>=90:
    print('Your Grade is: A+')
elif score>=80:
    print('Your Grade is: A')
elif score>=70:
    print('Your Grade is: B')
elif score >=60:
    print('Your Grade is: C')
elif score >=50:
    print('Your Grade is: D')
else:
    print('Your Grade is: F')



# Bonus: number checker.

num = int(input("Enter a number: "))

if num>0:
    print('Number is positive.')
elif num<0:
    print('Number is negative.')
else:
    print('Number is zero.')


if num%2==0:
    print('Number is even.')
else:
    print('Number is odd.')

if num%5==0:
    print('Number is divisible by 5.')
else:
    print('Number cannot be divisible by 5.')


# Bonus: type 2

num = int(input("Enter a number:"))
if num<0:
    if num%2==0:
        print(f'{num} is a negative even number.')
    else:
        print(f'{num} is a negative odd number.')
elif num>0:
    if num%2==0:
        print(f'{num} is a positive even number.')
    else:
        print(f'{num} is a positive odd number.')
else:
    print(f'{num} is an even number.')
