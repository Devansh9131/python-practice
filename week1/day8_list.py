# practice: list statistics
# Program 01


def list_statistics(numbers):
    if numbers.strip() == "":
        return "Please enter numbers."
    temp_list = numbers.split()
    numbers_list = [int(num) for num in temp_list]

    smallest = min(numbers_list)
    largest = max(numbers_list)
    total = sum(numbers_list)
    average = total / len(numbers_list)
    return f"Largest: {largest}\nSmallest: {smallest}\nAverage: {average}"


# Program 02


def smallest_num(numbers_list):
    smallest = numbers_list[0]
    for num in numbers_list:
        if num < smallest:
            smallest = num
    return smallest


def largest_num(numbers_list):
    largest = numbers_list[0]
    for num in numbers_list:
        if num > largest:
            largest = num
    return largest


def total_num(numbers_list):
    total = 0
    for num in numbers_list:
        total += num
    return total


def list_statistics2(numbers):
    if numbers.strip() == "":
        return "Please enter numbers."
    temp_list = numbers.split()
    numbers_list = [int(num) for num in temp_list]

    smallest = smallest_num(numbers_list)
    largest = largest_num(numbers_list)
    total = total_num(numbers_list)
    average = total / len(numbers_list)
    return f"Largest: {largest}\nSmallest: {smallest}\nAverage: {average}"


# INPUT
numbers = input("Enter numbers: ")
print(list_statistics(numbers))
print(list_statistics2(numbers))
