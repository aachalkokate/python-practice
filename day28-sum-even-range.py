start=int(input("enter starting number:"))
end=int(input("enter ending number:"))
sum = 0
for i in range(start,end + 1):
     if i % 2 != 0:
         sum = sum + i
print("sum of odd numbers=",sum)
