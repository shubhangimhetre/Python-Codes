from bs4 import BeautifulSoup
import json
import requests
from pprint import pprint
from Task1 import Moviedata
data=Moviedata()

def main_fun(data):
    
    def scrap_movie_cast(link,movie_name):
        d1={}
        link_data=requests.get(link)
        soup=BeautifulSoup(link_data.text,'html.parser')
        d1["Name"]=movie_name
        table=soup.find('div',class_='castSection')
        celebrity_link=table.find_all('a',class_="unstyled articleLink")
        # print(celebrity_link) 
        celebrity_name=table.find_all('span',class_='characters subtle smaller')
        # print(celebrity_name)
        # a_tag=table.find_all('a')
        d1={}
        d2={}
        dic={}
        for i in range(len(celebrity_link)):
            
            
            Name=celebrity_name[i]['title']
            # print(Name)
            if i==0:

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
                d1[cast_id]=Name 
                # print(d1)

            else:
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
            # d1['Co-Actors']=(d2)                     
        # print(d1)
            dic[movie_name]=d1
            dic['Co-Actors']=d2

        print(dic)
        return dic

    # def movie_filename(movie_name):
    #     filename=movie_name.json 
        
    #     return filename

    movie_cast_list=[]
    for i in data:
            for j in i:
                movie_name=i["Name"]
                if j=="link":
                    # print( i[j])
                    movie_details_dic=scrap_movie_cast(i[j],movie_name) 
                    movie_cast_list.append(movie_details_dic)
                    # movie_filename=str(movie_filename(movie_name))
                with open("2movie_cast14.json","w") as f:
                    json.dump(movie_cast_list,f,indent=3)
    # print(movie_cast_list)

data5=main_fun(data)