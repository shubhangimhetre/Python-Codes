i=0
while i<=6:
    j=0
    while j<=4:
        if((i==0 or i==3 or i==6) and (j>0 and j<4)) or (j==0 and (i>0 and i<3)) or (j==4 and (i>3 and i<6)):
            print("*",end=(" "))
        else:
            print(" ",end=(" "))
        j=j+1
    print()
    i=i+1