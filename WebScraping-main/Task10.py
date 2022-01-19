import json
with open("2Scrap_Movie_details4.json" ,"r") as f:
    data4=json.load(f)
# print(data4)

def lang_and_director(movies_list):

    directors_dic={}
    for movie in movies_list:
        for director in movie:
            if director=='Director':

                directors_dic[movie[director]]={}
    # print(directors_dic)
    for i in range(len(movies_list)):
        for director in directors_dic:
            if director in movies_list[i]['Director']:
                for language in movies_list[i]:
                    if language=='Original Language':
                        a=movies_list[i][language]
                        directors_dic[director][a]=0
    # print(directors_dic)
    for i in range(len(movies_list)):
        for director in directors_dic:
            # print(director)
            if director in movies_list[i]['Director']:               
                for language in movies_list[i]:
                    # print(language)
                    if language=='Original Language':
                        # print(movies_list[i][language])  
                        for l in directors_dic[director]:
                            # print(directors_dic[director][l])                    
                            directors_dic[director][l]+=1
    # print(directors_dic)
    return directors_dic

director_by_language=lang_and_director(data4)
with open("Director_by_language.json","w") as f:
    json.dump(director_by_language,f,indent=4)
print(director_by_language)
  







    