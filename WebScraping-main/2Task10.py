##Task 10= directors and languages 


import json
with open("2Scrap_Movie_details4.json" ,"r") as f:
    data4=json.load(f)
print(data4)


def language_fun(director_name):


    l1=[]
    for i in data4:
        for j in i:
            print(j)
            if i[j]==director_name:
                if j=="Original Language":
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






l1=[]
for i in data4:
    for j in i:
        print(j)
        if j=="Director":
            if i[j] not in l1:
                l1.append(i[j])
                language_dic=language_fun(i[j])
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


with open("directorcount1.json","w")  as f:
    json.dump(d1,f,indent=2) 


    


