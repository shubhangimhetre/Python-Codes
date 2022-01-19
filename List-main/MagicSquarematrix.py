# # 4.
# //MagicSquareMatrix
# // magic_square = [

# //     [8, 3, 4],

# //     [1, 5, 9],

# //     [6, 7, 2]

# // ]




# r=int(input("enter number of rows"))
# c=int(input("enter number of columns"))
# ms=[]
# sumd1=0
# sumd2=0
# sumr=0
# sumc=0
# if r==c:
#     i=0
#     for i in range(r):
#         j=0
#         b=[]
#         for j in range (c):
#              r1=int(input("enter elements of row"))
#              b.append(r1)
#         ms.append(b)
#     print(ms)
#     for i in range(r):
#         for j in range(c):
#             if i==j:
#                 sumd1=sumd1+ ms[i][j]  
#             if i+j==r-1:
#                 sumd2=sumd2+ms[i][j]           
#     if sumd1!=sumd2:
#         f=0
#     else:
#         for i in range(r):
#             sumr=0
#             sumc=0
#             for j in range(c):
#                 sumr=sumr+ms[i][j]
#                 sumc=sumc+ms[j][i]
#             # print(sumc)
#             # print(sumr)
#             if sumr!=sumd1:
#                    f=0
#             if sumc!=sumd1:
#                    f=0
#             else:
#                    f=1
#     if f==1:
#         print("Matrix is magic square")
#     else:
#         print("Matrix is not magic square") 
# else:
#    print("The given matrix is not square matrix") 