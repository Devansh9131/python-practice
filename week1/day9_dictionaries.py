# Practice 01: word counter


def word_counter(sentence):
    word_counts = {}
    sentence_list = sentence.lower().split()
    for word in sentence_list:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


sentence = input("Enter a sentence: ")  # the cat and the dog
for key, value in word_counter(sentence).items():
    print(f"{key}: {value}")

# Practice 02: remove duplicates
# Program 01


def remove_duplicates_set(numbers_list):
    numbers_set = set(numbers_list)
    new_numbers_list = list(numbers_set)
    return new_numbers_list


# Program 02


def remove_duplicates_loop(numbers_list):
    new_numbers_list = []
    for num in numbers_list:
        if num not in new_numbers_list:
            new_numbers_list.append(num)
    return new_numbers_list


numbers = input("Enter numbers: ")
numbers_list = [int(num) for num in numbers.split()]
print(f"Set version:\nWithout duplicates: {remove_duplicates_set(numbers_list)}")
print(f"Loop version:\nWithout duplicates: {remove_duplicates_loop(numbers_list)}")
