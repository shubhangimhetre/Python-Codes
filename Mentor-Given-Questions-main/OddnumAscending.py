##To arrange only odd numbers in ascending and keep even number as it is

# s=[2,9,1,8,5,11,3,4,7]
# i=0 
# b=[] 
# for i in range(len(s)):
#     if s[i]%2==0:
#         # print(s[i])
#         pass
#     else:
#         b.append(s[i])
#         b.sort()
# i=0
# for i in range(len(s)):
#     if s[i]%2==0:
#         a=s.index(s[i])
#         # print(a)
#         b.insert(a,s[i])
# print(b)


##without using sort function

#To arrange only odd numbers in ascending and keep even number as it is
# s=[2,9,1,8,5,11,3,4,7]
# i=0 
# b=[] 
# for i in range(len(s)):
#     if s[i]%2==0:
#         pass
#     else:
#         b.append(s[i])
# i=0  
# for i in range(len(b)):
#     j=i
#     temp=0
#     for j in range(len(b)): 
#         if b[j]>b[i]:
#             temp=b[i]
#             b[i]=b[j]
#             b[j]=temp   
# i=0
# for i in range(len(s)):
#     if s[i]%2==0:
#         a=s.index(s[i])
#         b.insert(a,s[i])
# print(b)





str1=input("enter your string")
str1=" "+str1
a=[]
a=list(str1)
print(a)
for i in range(len(a)):
    if a[i]==(' '):
       b=a[i+1]
       c=b.upper()
       print(b)

# print(a)

# str1="how are you"
# str2=str1.up\