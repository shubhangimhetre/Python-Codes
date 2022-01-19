# list1=["dewas",1,2,3.0,178,"yash"]
# list1.reverse()
# print(list1)

##8. to concatenate two list without using function

# list1=["M","na","i","ke"]
# list2=["y","me","s","lly"]
# list3=list1[0]+list2[0],list1[1]+list2[1],list1[2]+list2[2],list1[3]+list2[3]
# print(list3)

##9. take userinput and create list and reverse it

# size=int(input("enter number of items"))
# i=1
# list1=[]
# list2=[]
# while i<=size:
#     item=input("enter the item")
#     list1.append(item)
#     i=i+1
# print(list1)
# i=len(list1)-1
# while i>=0:
#     a=list1[i]
#     list2.append(a)
#     i=i-1
# print(list2)

##10. take userinput of numbers and turn every item of a list into its square

# size=int(input("enter number of items"))
# i=1
# list1=[]
# list2=[]
# while i<=size:
#     item=input("enter the item")
#     list1.append(item)
#     i=i+1
# print(list1)
# i=0
# while i<len(list1):
#      a=int(list1[i])**2
#      list2.append(a)
#      i=i+1
# print(list2)

##11. join indices

# list1=["Hello","take"]
# list2=["Dear","sir"]
# list3=[]
# i=0
# while i<len(list1):
#     j=0
#     while j<len(list2):
#          a=list1[i]+" "+list2[j]
#          list3.append(a)
#          j=j+1
#     i=i+1
# print(list3)

##12.iterate over both the value and indices

# grocery_list=['flour','cheese','carrots']
# for i in range(len(grocery_list)):
#     print(i,":",grocery_list[i])

##13. convert character matrix to single string

# list1=[['g','f','g',],['i','s'],['b','e','s','t']]
# import itertools
# flat_list=list(itertools.chain(*list1))
# print(flat_list)
# liststr="".join(flat_list)
# print(liststr)

##14.list product excluding duplicates

# list1=[6,1,3,5,6,3,1]
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)
# pdt=1
# i=0
# for i in range(len(list2)):
#      pdt=pdt*list2[i]
# print(pdt) 

##15. count unique values inside a list

# list1=[1,2,2,5,8,4,4,8]
# count=0
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
#         count=count+1
# print(count)

##first list in original order and second list in reverse order        

# list1=[1,2,3,4,5]
# list2=[6,7,8,9,0]
# i=0
# j=len(list2)-1 
# while i<len(list1):
#      print(list1[i])
#      i=i+1
# while j>=0:
#     print(list2[j]) 
#     j=j-1   

# size=int(input("enter number of items for first list"))
# i=1
# list1=[]
# list2=[]
# while i<=size:
#     item=input("enter the item")
#     list1.append(item)
#     i=i+1
# print(list1)
# size2=int(input("enter number of items for second list"))
# i=1
# while i<=size2:
#     item=input("enter the item")
#     list2.append(item)
#     i=i+1
# print(list2)
# i=0
# j=len(list2)-1 
# print("Items of first list")
# while i<len(list1):
#      print(list1[i])
#      i=i+1
# print("Items of second list")
# while j>=0:
#     print(list2[j]) 
#     j=j-1  