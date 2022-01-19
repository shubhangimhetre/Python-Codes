# # Q.9 Apki pass ek shopping name ki ek dictionary hai
# # {
# #     "shopping_list":
# #         { 
# #             "chaco":"15",
# #             "Biscuits":"50",
# #             "Diary_milk":"30",
# #             "ice_cream":"20",
# #         } 
# # }

# # Apki dictionary ka use kar ke ek json file create karna hai. 
# # Aur apko kuch task perform karne hai jaise ki
# # main dekhna chahta hu shopping list ko json file dekhna.
# # phir main user se poochu ga ki kon sa item khareedna chahte ho.
# # uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho.
# # phir aapka wo number of items json file se remove karna hai.
# # Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga.
# # Output:-
# # show shopping_list:- 
# # {
# #     "shopping_list":{ 
# #         "chaco":"15",
# #         "Biscuits":"50",
# #         "Diary_milk":"30",
# #         "ice_cream":"20",
# #          } 
# # }

# import json
# import os

# def shopping(dic1,dic2):
#     Path_exist=os.path.exists("Shopping.json")
#     if Path_exist==False:        
#         dic1["shopping"]=dic2
#         item=input("enter the item that you want to buy: ")
#         num_items=int(input("enter the number of items: "))
#         dic2[item]=num_items
#         user_input=input("Do you want to add more item, enter y or n: ")
#         if user_input=="y":
#             shopping(dic1,dic2)
#             with open ("Shopping.json","w") as f:
#                 json.dump(dic1,f)  
#         else:
#             print("Ok, Done")       

#     elif Path_exist==True:
#         dic1["shopping"]=dic2
#         item=input("enter the item that you want to buy: ")
#         num_items=int(input("enter the number of items: "))

#         with open ("Shopping.json","r") as f:
#             data=json.load(f) 
#             if item in data:           
#                 for i in data:
#                     for j in data[i]:

#                         data[i][item]=num_items
#                         with open("Shopping.json","w") as f:
#                             json.dump(data,f)

#             else:
#                 data["shopping"][item]=num_items
#                 with open("Shopping.json","w") as f:
#                     json.dump(data,f)

                    
#         with open("Shopping.json","w") as f:
#             json.dump(data,f)

#         user_input=input("Do you want to add more item, enter y or n: ")
#         if user_input=="y":
#             shopping(dic1,dic2)
#         else:
#             print("Ok,Done")

# dic1={}
# dic2={}
# shopping(dic1,dic2)

