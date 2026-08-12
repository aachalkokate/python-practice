
num = 65

for i in range(1, 6):
    for j in range(i):
        print(chr(num), end="")
        num = num + 1

        if j != i - 1:
            print("*", end="")

    print()
