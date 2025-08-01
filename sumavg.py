l = []
n = int(input("enter no.of elements"))
for i in range(n):
  ele = int(input("enter element"))
  l.append(ele)
print(l)
sum = sum(l)
print(sum)
avg = sum/len(l)
print(avg)
