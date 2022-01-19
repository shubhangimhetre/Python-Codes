from Task1 import Moviedata
import json
data=Moviedata()
# print(data)
def MovieByYear(data):

    # print(data)
    years_list=[]
    for i in data:
        for j in i:
            if j=="Year":
                # print(i[j])
                if i[j] not in years_list:
                    years_list.append(i[j])
    years_list.sort()
    # print(years_list)
    Movie_year={i:[] for i in years_list}
    for i in data:
       
        year=i['Year']
        for x in Movie_year:
            if str(x)==str(year):

                Movie_year[x].append(i)
                
    print(Movie_year)
    with open("MovieByYear.json","w") as f:
        json.dump(Movie_year,f,indent=4)
    return Movie_year

data2=MovieByYear(data)


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
                        print(y)
                        moviedec[i].append(y)
        # return(moviedec)
    with open("Movies_by_decade3.json","w") as f:
        json.dump(moviedec,f,indent=4)
    return moviedec


data3=Movie_decade(data2)
