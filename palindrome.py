str="MADAM"
rev_string=''
for i in str:
	rev_string=i+rev_string
print(rev_string)
if rev_string==str:
	print(str,"is a palindrome")
else:
	print(str,"is not a palindrome")

