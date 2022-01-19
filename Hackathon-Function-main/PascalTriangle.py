# def pascal():
#     n=int(input("enter the number of rows"))
#     a=[]
#     i=0
#     for i in range(n):
#         b=[]
#         j=0
#         for j in range(i+1):
#             if j==0 or j==i:
#                 b.append(1)
#             else:
#                 b.append(a[i-1][j-1]+a[i-1][j])
#             # print(b)
#         a.append(b)
#     print(a)      
# pascal()




# def pascal():
#     n=int(input("enter the number of rows"))
#     a=[]
#     i=0
#     for i in range(n):
#         b=[]
#         j=0
#         for j in range(i+1):
#             if j==0 or j==i:
#                 b.append(1)
#             else:
#                 b.append(a[i-1][j-1]+a[i-1][j])
#             # print(b)
#         a.append(b)
#     print(a) 
#     i=0
#     while i<len(a):
#         b=1
#         while b<=len(a)-i:
#             print(" ",end=(" "))
#             b=b+1
#         j=0
#         while j<i+1:
#             print(a[i][j]," ", end=(" "))
#             j=j+1
#         print()
#         i=i+1  
# pascal()






    

