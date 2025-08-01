l=[]
n=int(input("enter the size of the list:"))
for i in range(n):
        i=int(input("enter the element:"))
        l.append(i)
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even:",even)
print("odd:",odd)        
