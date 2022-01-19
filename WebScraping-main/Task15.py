import json


with open ("movie_cast.json","r") as f:
    movie_cast_list=json.load(f)
# print(movie_cast_list)

cast_name_list=[]
for i in range(len(movie_cast_list)):
    # print(i)
    for j in movie_cast_list [i].values():
        # print(j)
        for k in j.values():
        
            # print(k)
            if k not in cast_name_list:
                cast_name_list.append(k)        
# print(cast_name_list)




cast_id_list=[]
for i in range(len(movie_cast_list)):
    # print(i)
    for j in movie_cast_list [i].values():
        # print(j)
        for k in j:
        
            # print(k)
            if k not in cast_id_list:
                cast_id_list.append(k)        
# print(cast_id_list)
# for i in cast_name_list:

cast_item_count=[]
for i in cast_name_list:
    c=0
    for m in range(len(movie_cast_list)):
        for j in movie_cast_list [m].values():
            for k in j.values():  
                # print(k)         
                if k ==i:
                    # print(i)
                    c=c+1
    cast_item_count.append(c)     
print(cast_item_count)


dic={}
for i in range(len(cast_id_list)):
    d1={}
    # dic[i]=d1
    # for j in range(len(cast_name_list)):
    d1["Name"]=cast_name_list[i]
    d1["Num Of Movies"]=cast_item_count[i]
    dic[cast_id_list[i]]=d1
print(dic)


with open("Task15.json","w") as f:
    json.dump(dic,f,indent=4)
    



                 



