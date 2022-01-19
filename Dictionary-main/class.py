# #1.
# dict={1:"one",2:"two",3:"three"}
# print(dict)

# #2.
# print(len(dict))
# #o/p=3

# #3. access 
# # get values of specific item
# x=dict[1]
# y=dict[2]
# print(x,y)
# #another method
# z=dict.get(1)
# print(z)


# #get keys 
# x=dict.keys()
# print(x)
# ##it will print the list of keys
# #o/p= dict_keys([1,2,3])
 
# #get values

# j=dict.values()
# print(j)
# print(dict.values())
# #o/p=dict_values(['one','two','three'])


# #get items
# k=dict.items()
# print(k)
# #o/p=dict_items([(1,'one'),(2,'two'),(3,'three')])


# #check if a specified key is present in dict
# if 1 in dict:
#     print("yes")
# else:
#     print("no")




# #change items

# #Direct method
# dict[1]=10
# print(dict)

# #update
# dict.update({1:'one'})
# print(dict)


# #add
# dict[4]='four'
# print(dict)

# #remove

# #pop()
# # #removes item with specified key name
# # dict.pop(1)
# # print(dict)

# # #popitem() method removes the last inserted item
# # dict.popitem()
# # print(dict)

# # #del keyword
# # del dict[2]
# # print(dict)


# # del dict
# # print(dict)

# # dict.clear()
# # print(dict)




# ###loop

# # # for loop

# # for x in dict:
# #     print(x)

# # for x in dict:
# #     print(dict[x])


# # for x in dict.keys():
# #     print(x)
# # #it will return keys

# # for x in dict.values():
# #     print(x)
# # # #it will return values

# # for x,y in dict.items():
# #     print(x,y)
# # ##1  one
# # ##2  two
# # #it will return this type of key value



# # #Copy dict
# # # you cant copy By dict1=dict
# # mydict=dict.copy()
# # print(mydict)
# # mydict[5]='five'
# # print(mydict)
# # print(dict)

# # #Another way
# # mydict=dict(dict)
# # print(mydict)


# # dic1={1:{1:'one',2:'two'},2:{2:'two',3:'three'},3:{3:'three',4:'four'}}
# # d1={1:'one',2:'two'}
# # d2={2:'two',3:'three'}
# # d3={3:'three',4:'four'}
# # dic={1:d1,2:d2,3:d3}
# # print(dic)
# # print(dic1)

# ##Simple accesing nested
# # print(dic1[1][2])



# # dic1={1:{1:'one',2:'two'},2:{2:'two',3:'three'},3:{3:'three',4:'four'}}
# # for x in dic1.values():
# #     for j in x:
# #         print(j)

# # for x in dic1:
# #     for j in dic1[x].values():
# #         print(j)


# # sum=0
# # for i in dic1.keys():
# #     sum=sum+i
# # print(sum)
    
# # sum=0
# # for i in dic1.values():
# #     for j in i.keys():
# #         sum=sum+j
# # print(sum)



# # dic={1:'one',2:'two'}
# # del dic
# # print(dic)


# dic1={1:{1:'one',2:'two'},2:[1,2,3,4,5,6],3:{3:'three',4:'four'}}

