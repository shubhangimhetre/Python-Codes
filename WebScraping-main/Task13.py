

from bs4 import BeautifulSoup
import json
import requests
from pprint import pprint
from Task1 import Moviedata
data=Moviedata()


def Main_fun(data): 
    # Scrap_data_list=[]
    def Scrap_movie_details(link,MovieName):
        d1={}
        link_data=requests.get(link)

        soup=BeautifulSoup(link_data.text,'html.parser')     
        d1["Name"]=MovieName
        movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()     
        d1["Bio"]=movie_bio
        alltitle=soup.find_all("div",class_="meta-label subtle")
        allvalue=soup.find_all("div",class_="meta-value")
        

        for i in range(len(alltitle)):
            d1[str(alltitle[i].get_text().strip())[:-1]]=allvalue[i].get_text().strip()
        
        return d1
    movie_details_list=[]

    def cast_func(link,movie_name):
        d1={}
        link_data=requests.get(link)
        soup=BeautifulSoup(link_data.text,'html.parser')
        # d1["Name"]=movie_name
        table=soup.find('div',class_='castSection')
        celebrity_link=table.find_all('a',class_="unstyled articleLink")
        # print(celebrity_link) 
        celebrity_name=table.find_all('span',class_='characters subtle smaller')
        # print(celebrity_name)
        d2={}
        dic={}
        for i in range(len(celebrity_link)):
            
            
            Name=celebrity_name[i]['title']
            # print(Name)
            link="https://www.rottentomatoes.com/"+celebrity_link[i]['href']
            cast_id=""
            id=len(link)-1

            while id>=0:
                if link[id]!="/":
                    cast_id+=link[id]
                else:
                    break
                id=id-1
            cast_id=list(cast_id)
            cast_id.reverse()
            cast_id=''.join(cast_id)
            # print(cast_id)
            d2[cast_id]=Name           
        # print(d1)
            # dic["cast"]=d2
        # print(dic)
        return d2

    
    for i in data:
        for j in i:
            MovieName=i["Name"]
            if j=="link":
                # print( i[j])
             
                movie_details_dic=Scrap_movie_details(i[j],MovieName)   
                cast_details_dic=cast_func(i[j],MovieName)
                movie_details_dic['Cast']=cast_details_dic

                movie_details_list.append(movie_details_dic)

    # print(movie_details_list)
    # top10movies=movie_details_list[:10]
    # # print(top10movies)ains constant for that object throughout its lifetime.

    # with open("Top10.json","w") as f:
    #     json.dump(top10movies,f,indent=4)

    with open("Scrap_Movie&cast.json","w") as f:
        json.dump(movie_details_list,f,indent=4)
    return movie_details_list
        
data4=Main_fun(data)

 
