
# from bs4 import BeautifulSoup
# import json
# import requests
# from pprint import pprint
# from Task1 import Moviedata
# data=Moviedata()
# # print(data)



# def Main_fun(data):
#     Scrap_data_list=[]
#     def Scrap_movie_details(link,MovieName):
#         d1={}
#         link_data=requests.get(link)
#         # print(link_data.get_text())
#         soup=BeautifulSoup(link_data.text,'html.parser')
#         # print(soup)
        
#         d1["Name"]=MovieName

#         movie_bio=soup.find("div",class_="movie_synopsis clamp clamp-6 js-clamp").get_text().strip()     
#         # print(movie_bio)
#         d1["Bio"]=movie_bio
#         language=soup.find("div",class_="meta-value").get_text()
#         # d1["Language"]=language
#         # print(d1)
#         director_list=[]
#         director=soup.find_all("a")
#         # for i in director:
#         #     dname=director[i].get_text()
#         #     director_list.append(dname)
#         # print(director_list)

#     movie_details_list=[]
#     # print(data)
#     for i in data:
#         # print(data[i]["link"])
#         for j in i:
            
#             MovieName=i["Name"]
#             if j=="link":
#                 # print(i[j])
#                 movie_details_dic=Scrap_movie_details(i[j],MovieName)
#                 # movie_details_list.append(movie_details_dic)
#     # with open("Scrap_Movie_details4.json","w") as f:
#     #     json.dump(movie_details_list,f)
#     #     return movie_details_list
# data4=Main_fun(data)





from bs4 import BeautifulSoup
import json
import requests
from pprint import pprint
from Task1 import Moviedata
data=Moviedata()
# print(data)

def Main_fun(data):
    Scrap_data_list=[]
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
            d1[alltitle[i].get_text().strip()]=allvalue[i].get_text().strip()
        # pprint(d1)
        return d1

    movie_details_list=[]
    # # print(data)

    
        # print(data[i]["link"])
    for i in data:
        for j in i:
            MovieName=i["Name"]
            if j=="link":
                # print(i[j])
                movie_details_dic=Scrap_movie_details(i[j],MovieName)
                # print(movie_details_dic)
                
                movie_details_list.append(movie_details_dic)

    print(movie_details_list)

    with open("2Scrap_Movie_details4.json","w") as f:
        json.dump(movie_details_list,f,indent=4)
        
data4=Main_fun(data)

