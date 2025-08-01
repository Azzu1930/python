n=int(input())
d=n
rev=0
while(d>0):
    rem=d%10
    rev=rev*10+rem
    d=d//10
if(rev==n):
    print(n,"is palindrome")
else:
    print(n,"is not palindrome")
