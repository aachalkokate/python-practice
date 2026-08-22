num = int(input("enter your number:"))
sum = 0

while num > 0:
    digit = num%10

    if digit % 2 != 0:
        sum = sum + digit
        
    num = num // 10
    
print("sum of odd digits:",sum)



