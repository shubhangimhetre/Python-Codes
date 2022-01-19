# with open("words.txt","r") as f:
#     data=f.read()
#     print(data)
# words_list=data.split()
# print(words_list)

import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)