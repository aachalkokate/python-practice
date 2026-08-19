num=int(input("enter your number:"))
original = num
sum = 0

while num != 0:
    digit = num % 10
    num = num // 10

    fact = 1

    for i in range (1,digit + 1):
        fact = fact * i
        
    sum = sum + fact

if original == sum:
    print("strong number")
else:
    print("not strong number")

 
