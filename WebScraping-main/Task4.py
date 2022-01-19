from bs4 import BeautifulSoup
import json
import requests
from pprint import pprint
# from Task1 import Moviedata
# data=Moviedata()
# # print(data)
movie_details_list=[]
def Scrap_movie_details(link):
    d1={}
    link_data=requests.get(link)
    soup=BeautifulSoup(link_data.text,'html.parser') 
    d1["Name"]="Black Panther"   
    movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()
    d1["Bio"]=movie_bio
    alltitle=soup.find_all("div",class_="meta-label subtle")
    allvalue=soup.find_all("div",class_="meta-value")
         
    for i in range(len(alltitle)):
        d1[str(alltitle[i].get_text().strip())[:-1]]=allvalue[i].get_text().strip()
    # pprint(d1)
    movie_details_list.append(d1)
    with open("Scrap_Movie_details4.json","w") as f:
        json.dump(movie_details_list,f,indent=4)

link="https://www.rottentomatoes.com//m/black_panther_2018"
data4=Scrap_movie_details(link)


