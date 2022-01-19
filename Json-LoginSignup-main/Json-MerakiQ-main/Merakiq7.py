# # Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
# # Example:
# # Input :-
# # Text.txt:-  
# #  Name Abhishek
# #  Designation CEO of navgurukul
# #  Gender male
# #  Age 29

# # Output:-

# # Json_file.json:-
# # {
# #     “Name”: “Abhishek”,
# #     “Designation”: “CEO of      navgurukul”,
# #     “Gender”:”male”,
# #     “Age”: “29”
# #     }

# import json
# text_file=open("txt_file.txt","w")
# text_file.write('''Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29''')
# text_file.close()
# d={}

# with open("Text_json.json","w") as f:
#     json.dump(d,f,indent=4)
# f.close

