for i in range (4,-1,-1):
    for j in range (4-i):
        print(" ",end="")

    for j in range(2*i+1):
        print(chr(65+i),end="")
    print()
