num = int(input("enter your number:"))
original = num
square = num * num
sum = 0

while square != 0:
    digit = square % 10
    sum = sum + digit
    square = square // 10

if sum == original:
    print("Neon number")
else:
    print("Not Neon number")

