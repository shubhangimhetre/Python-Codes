n=4
i=0
while i<4:
    b=2
    while b<=n-i:
        print(" ",end=(""))
        b=b+1
    j=0
    while j<=i:
        print("* ",end=(""))
        j=j+1
    b=3
    while b<=2*(n-i):
        print(" ",end=(""))
        b=b+1 
    j=0
    while j<=i:
        print("* ",end=(""))
        j=j+1
    
    print()
    i=i+1 

i=8
while i>0:
    b=0
    while b<8-i:
        print(" ",end=(""))
        b=b+1
    j=i
    while j>0:
        print("* ",end=(""))
        j=j-1
    i=i-1
    print()
 

 