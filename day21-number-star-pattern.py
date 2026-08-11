num=1
for i in range(1,6):
    for j in range(1,i+1):
        if j==i:
            print(j,end="")
        else:
            print(j,end="*")
    print()
            
