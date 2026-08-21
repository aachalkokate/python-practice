num = int(input("enter your number:"))
square = num * num
digits = len(str(num))
last = square % (10 ** digits)

if last == num:
    print("Automorphic number")
else:
    print("not Automorphic number")

