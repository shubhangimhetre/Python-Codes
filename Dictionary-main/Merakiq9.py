# #  Store the unique letters and 
# # their frequency of the letters from the word "MISSISSIPPI" to a dictionary,
# #  were the letters are the keys and their frequencies are the values.
# # {'M':1,'I':4,'S':4,'P':2}
# # str="MISSISSIPPI"

# str=list("MISSISSIPPI")
# list1=[]
# dic={}
# for i in str:
#     if i not in dic:
#         list1.append(i)
#         c=0
#         for j in str:
#             if i == j:
#                c=c+1
#         dic[i]=c
# print(dic)