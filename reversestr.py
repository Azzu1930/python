def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s
input_str = input("Enter a string: ")
print("Reversed string:", reverse_string(input_str))
