# # Q.1 Json data ko python object main convert karne ka program likho?.

# # Example:
# # Input :- {"Name":"Ram","Class":"IV", "Age":9 }'

# # Output :-{'Name': 'Ram','Class': 'IV', 'Age': 9
# # }


# import json

# dic1={"Name":"Ram","Class":"IV", "Age":9 }
# text_file=open("myfile.json","w")
# json.dump(dic1,text_file)
# text_file.close()



# text_file=open("myfile.json","r")
# a=json.load(text_file)
# text_file.close()
# print(a)