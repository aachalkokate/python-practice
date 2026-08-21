start=int(input("enter starting number:"))
end=int(input("enter ending number:"))
even= 0
odd=0
for i in range(start,end + 1):
     if i % 2 != 0:
         odd = odd + 1
     else:
         even = even + 1
print("even numbers=",even)
print("odd numberes=",odd)
