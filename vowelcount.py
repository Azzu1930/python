def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char in vowels)
input_str = input("Enter a string: ")
print("Number of vowels:", count_vowels(input_str))
