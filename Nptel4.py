def magic_square(n):
    magicSquare=[]
    for i in range(n):
        col=[]
        for j in range(n):
            col.append(0)
        magicSquare.append(col)

    count=1
    num=n*n
    i=n//2
    j=n-1
    while(count<=num):
        if(i==-1 and j==n):
            i=0
            j=n-2
        else:
            if(i==-1):
                i=n-1
            if(j==n):
                j=0
        if(magicSquare[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
            magicSquare[i][j]=count
            count=count+1

        i=i-1
        j=j+1

    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print()

magic_square(3)