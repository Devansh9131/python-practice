# Program 1: Palindrome checker


def is_palindrome(text):
    cleaned_text = text.replace(" ", "").lower()
    reverse_text = cleaned_text[::-1]
    if len(cleaned_text) == 1:
        return f"{text} is a palindrome."
    if cleaned_text == reverse_text:
        return f"{text} is a palindrome."

    return f"{text} is not a palindrome."


text = input("Enter a word: ")

print(is_palindrome(text))

print("\n")


# Program 2: Vowel counter


def count_vowel(sentence):
    count = 0
    cleaned_text = sentence.lower()
    for char in cleaned_text:
        if char in "aeiou":
            count += 1

    return f"Number of vowels: {count}"


sentence = input("Enter a sentence: ")
print(count_vowel(sentence))

print("\n")
