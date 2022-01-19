
from Task1 import Moviedata
import json
data=Moviedata()
# print(data)
from Task2 import MovieByYear
data2=MovieByYear(data)
# print(data2)


def Movie_decade(data2):
    # print(data2)
    moviedec={}
    list1=[]
    for i in data2:
        mod=i%10
        decade=i-mod
        if decade not in list1:
            list1.append(decade)
        list1.sort()
        for i in list1:
            moviedec[i]=[]
        for i in moviedec:
            decade10=i+9
            for x in data2:
                if x<=decade10 and x>=i:
                    for y in data2[x]:
                        # print(y)
                        moviedec[i].append(y)

    with open("Movies_by_decade4.json","w") as f:
        json.dump(moviedec,f,indent=4)
    return moviedec


data3=Movie_decade(data2)







