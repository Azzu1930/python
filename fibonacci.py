n=int(input())
fib1=0
fib2=1
if(n==1):
    print(0)
elif(n==2):
    print(0,1)
else:
    print(0,1,end=' ')
    for i in range((n-2)+1):
       fib=fib1+fib2
       print(fib,end=' ')
       fib1=fib2
       fib2=fib
       
       
    
