
def count_vowels(input_string):
    vowels = "aeiou"
    count = sum(1 for char in input_string.lower() if char in vowels)
    return count
