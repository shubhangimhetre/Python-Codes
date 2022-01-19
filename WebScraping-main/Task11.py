
import json
with open("2Scrap_Movie_details4.json" ,"r") as f:
    data4=json.load(f)
# print(data4)




l1=[]
for i in data4:
    for j in i:
        # print(j)
        if j=="Genre":
            a=i[j].strip().split()
            # print(a)
            for x in a:
                # print(x)               
                    # print(l1)
                    if x[-1]==',':
                        x=x[:-1]
                        # print(x)
                        if x not in l1:
                            l1.append(x)
                    if x not in l1:  
                        if len(x)>1:
                            l1.append(x)
# print(l1)
l2=[]
for i in l1:
    c=0
    for k in data4:
        for j in k:
            if j=="Genre":
                a=k[j].strip().split()
            # print(a)
                for x in a:
                    if x[-1]==',':
                        x=x[:-1]
                        
                    if x==k[j]:
                        c=c+1
                        l2.append(c)
# print(l2)
d1={}

for j in range(len(l1)):
    d1[l1[j]]=l2[j]
print(d1)


with open("Genre_count.json","w")  as f:
    json.dump(d1,f,indent=2) 


         

