num = int(input("Enter your number:"))
found_zero = False

while num > 0:
    digit = num % 10

    if digit == 0:
        found_zero = True

    num = num // 10

if found_zero:
    print("Duck Number")
else:
    print("Not a Duck Number")


