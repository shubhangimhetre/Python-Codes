
from bs4 import BeautifulSoup
import json
import requests
from pprint import pprint
from Task1 import Moviedata
import os,time
import random
data=Moviedata()


def Main_fun(data): 

    Scrap_data_list=[]
    def Scrap_movie_details(link,MovieName):
        d1={}       
        random_sleep=random.randint(1,3)
        movie_id=""
        id=len(link)-1

        while id>=0:
            if link[id]!="/":
                movie_id+=link[id]
            else:
                break
            id=id-1
        movie_id=list(movie_id)
        movie_id.reverse()
        movie_id=''.join(movie_id)

        filename=movie_id+'.json'
        text=None

        # print(movie_id)
        if os.path.exists(filename):
            with open(filename,"r") as f:
                text=f.read()
            return text
        if text==None:

            time.sleep(random_sleep)
            link_data=requests.get(link)

            soup=BeautifulSoup(link_data.text,'html.parser')     
            d1["Name"]=MovieName
            movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()     
            d1["Bio"]=movie_bio
            alltitle=soup.find_all("div",class_="meta-label subtle")
            allvalue=soup.find_all("div",class_="meta-value")

            for i in range(len(alltitle)):
                
                d1[str(alltitle[i].get_text().strip())[:-1]]=allvalue[i].get_text().strip()
            # movie_details_list.append(d1)
            with open(filename,"w") as f:
                json.dump(d1,f,indent=4)
            return d1
    for i in data:
        for j in i:
            MovieName=i["Name"]
            if j=="link":
                # print( i[j])
             
                Scrap_movie_details(i[j],MovieName)                              
                
data4=Main_fun(data)
       
# 

 
