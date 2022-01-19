#question= find posiible combination in given list input=[1,2,3] output=[[],[1,2],[1,3],[2,1],[2,3],[3,1],[3,2]]

num=int(input("Enter the number of items of list: "))
i=0
c=1
l=[]
l3=[]
while i <num:
    n=int(input("Enter the number: "))
    l.append(n)
    i=i+1
print(l)
i=0
while i<len(l):
    for j in l:
        for k in l:
            l2=[]
            if l2 not in l3:
                l3.append(l2)
            if j!=k:
                l2.append(j)
                l2.append(k)               
                if l2 not in l3:
                    l3.append(l2)
                    c=c+1
    i=i+1
print(l3)
print(c)
    

        

        
        
