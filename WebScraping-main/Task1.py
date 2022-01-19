# # url = "https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"

# import requests
# from bs4 import BeautifulSoup
# import json

# url = "https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
# page=requests.get(url)

# soup=BeautifulSoup(page.text,'html.parser')
# # print(soup)
# Table=soup.find("table",class_="table").get_text()
# # print(Table)
# trs=soup.find_all("tr")
# # print(trs)
# TopMovies=[]
# for i in trs:
#     movie_rank=i.find_all("td",class_="bold")
#     # print(movie_rank)
#     d1={}
#     for j in movie_rank:
#         rank=j.get_text()
#         d1["Rank"]=rank
#         # print(rank)
#     movie_rating=i.find_all("span",class_="tMeterScore")
#     for j in movie_rating:
#         rating=j.get_text().strip()
#         d1["Rating"]=rating
#         # print(rating)
#     movie_name=i.find_all("a",class_="unstyled articleLink")
#     # print(movie_name)
#     for j in movie_name:
#         name=j.get_text().strip()
#         # print(name)
#         d1["Name"]=name

#     TopMovies.append(d1)
# print(TopMovies)

    


# with open("TopMovies.json","a") as f:
#     json.dump(TopMovies,f)

        
#     # for k in movie_name:
#     #     year=j.get_text().strip





import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

# def Moviedata():
url = "https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
# print(soup)
Table=soup.find("table",class_="table")

TopMovies=[]
movie_rank=Table.find_all("td",class_="bold")
movie_rating=Table.find_all("span",class_="tMeterScore")
movie_name=Table.find_all("a",class_="unstyled articleLink")  
movie_review=Table.find_all("td",class_="right hidden-xs")
movie_link=Table.find_all("tr")
# print(movie_link)
linklist=[]
# for i in movie_link:
    # print(i)
    # alltd=i.find_all("td")
    # print(alltd)
    # for j in alltd:
    #     print(j)
    # url=i.find("a",class_="unstyled articlelink")
#     link=url['href'].get_text()
#     print(link) 
#     linklist.append(link)
# print(linklist) 
    # linklist.append(i.find('a').get('href'))
    # print(linklist)


for i in range(0,len(movie_rank)):
    d1={}
    rank=movie_rank[i].get_text()
    rank=rank[:-1]
    d1["Rank"]=rank
    d1["Rating"]=movie_rating[i].get_text().strip()
    d1["Review"]=movie_review[i].get_text()
    d1["link"]="https://www.rottentomatoes.com/"+movie_name[i]['href']
    name=movie_name[i].get_text().strip()
    n1=name[0:-6]
    d1["Name"]=n1
    # print(n)
    list=name.split()
    year=list[-1][1:5]
    d1["Year"]=int(year)

    TopMovies.append(d1)
with open("TopMovies.json","w") as f:
    json.dump(TopMovies,f,indent=3)
#     # return  TopMovies
# Moviedata()
# print(Data)
    










