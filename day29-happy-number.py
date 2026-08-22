num = int(input("Enter your number:"))

while num > 9:
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit * digit
        num = num // 10

    num = sum
if num == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")


