import json
with open("2Scrap_Movie_details4.json" ,"r") as f:
    data4=json.load(f)
print(data4)

#Task6= Language and their count


# l1=[]
# for i in data4:
#     for j in i:
#         print(j)
#         if j=="Original Language":
#             if i[j] not in l1:
#                 l1.append(i[j])
# # print(l1)
# c=0
# l2=[]
# for i in l1:
#     c=0
#     for k in data4:
#         for j in k:
#             if i==k[j]:
#                 c=c+1
#     l2.append(c)
# # print(l2)

# d1={}

# for j in range(len(l2)):
#     d1[l1[j]]=l2[j]
# print(d1)

# with open("langcount.json","w")  as f:
#     json.dump(d1,f,indent=2)

#Task 7 = director and their movie count



l1=[]
for i in data4:
    for j in i:
        print(j)
        if j=="Director":
            if i[j] not in l1:
                l1.append(i[j])
# print(l1)
c=0
l2=[]
for i in l1:
    c=0
    for k in data4:
        for j in k:
            if i==k[j]:
                c=c+1
    l2.append(c)
# print(l2)

d1={}

for j in range(len(l2)):
    d1[l1[j]]=l2[j]
print(d1)

with open("directorcount.json","w")  as f:
    json.dump(d1,f,indent=2) 


         
