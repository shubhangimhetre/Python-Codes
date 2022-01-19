# # Q.2 Python object ko json data main convert karne ka program likho?

# # Example:
# # Input :- {"name": "David","class":"I", "age": 6}
# # Output:- {"name": "David","class": "I", "age": 6}

# import json
# dic1={"name": "David","class":"I", "age": 6}

# text_file=open("myfile.json","w")
# json.dump(dic1,text_file)
# text_file.close()
# text_file=open("myfile.json","r")
# print(json.load(text_file))
# text_file.close()

