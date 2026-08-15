num=int(input("enter your number:"))
original = num
rev=0
while num!=0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if original == rev:
    print("palindrome")
else:
    print("not palindrome")
 
