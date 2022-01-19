#if second digit is w2 then append that number in list2



n=int(input("enter the number of items: "))
i=1
list1=[]
while i <=n:
    num=int(input("enter the number: "))
    list1.append(num)
    i=i+1
# print(list1)
list2=[]
for i in list1:
    n=str(i)
    print(n[1])
 
    if n[1]==str(2):
        list2.append(i)
print(list2)