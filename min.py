l = []
n = int(input("enter the no of elements in the list:"))
for i in range(n):
   ele = int(input("enter the elements"))
   l.append(ele)
print("list = ",l)
print("maximum element = ",max(l))
print("minimum element = ",min(l))
print("the position of maximum element",l.index(max(l)))
print("the position of minimum element",l.index(min(l)))
