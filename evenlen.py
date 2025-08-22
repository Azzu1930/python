def print_even_length_words(s):
    words = s.split()
    even_length_words = [word for word in words if len(word) % 2 == 0]
    print("Even length words:", even_length_words)
input_str = input("Enter a string: ")
print_even_length_words(input_str)
