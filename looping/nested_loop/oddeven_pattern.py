for row in range(1,6):
    for column in range(1,row+1):
        print("O" if column%2!=0 else "E",end="\t")
    print()