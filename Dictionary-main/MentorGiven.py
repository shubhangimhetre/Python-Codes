##Acces the value of key 'history' from the below dict:
# sampledict={"class":{"student":{"name":"mike","Marks":{"Physics":70,"History":80}}}}
# for i in sampledict:
#     # print(i)
#     for j in sampledict[i]:
#         # print(j)
#         for k in sampledict[i][j].values():
#             if type(k)==dict:
#                 for l in k.keys():
#                     if l=="History":
#                         print(k[l])

            

##change brad's salary to 8500 from a given python dictionary
# sampledict={'emp1':{'name':'john','salary':7500},'emp2':{'name':'Emma','salary':8000},'emp3':{'name':'Brad','salary':6500}}
# for i in sampledict:
#     for j in sampledict[i]:
#         if sampledict[i][j]==6500:
#             sampledict[i][j]=8500            
#         print(sampledict[i][j])


# list1=[1,2,3,4,5]
# ## output={1:{2:{3:{4:{5:{}}}}}}
# b={}
# for i in list1[::-1]:
#     b={i:b}
# print(b)
    





# list1=[1,2,3,4,5,6,7,8,9,0]
# dic1={}
# i=0
# while i<len(list1):
#     j=i+1
#     list2=[]
#     while j<len(list1):
#         list2.append(list1[j])
#         j=j+1
#     dic1[list1[i]]=list2
#     i=i+1
# print(dic1)