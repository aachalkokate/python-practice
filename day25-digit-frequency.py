num = int(input("enter your number:"))
target=int(input("enter digit to find:"))
count = 0

while num != 0:
    digit = num % 10
    
    if digit == target:
        count = count + 1
        
  
    num = num // 10
 
print("frequency=", count)
