##Q1. What would be the output of the below code snippet ?
# a = {(1,2):1,(2,3):2}
# print(a[1,2])
# # options:
# # A. Key Error
# # B. 1 =ans
# # C. {(2,3):2}
# # D. {(1,2):1}

##Q2. What would be the output of the below code snippet ?
# a = {'a':1,'b':2,'c':3}
# print (a['a','b'])
# # Options :- 
# # A. Key Error=ans
# # B. [1,2]
# # C. {‘a’:1,’b’:2}
# # D. (1,2)


##Q3.What would be the output of the below code snippet ?
##question3_key2
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')
# print (len(fruit))
# print(fruit)
# output= {'Apple':2,'Banana':1,'apple';1}


##Q4.What would be the output of the below code snippet ?
##question4_key2
# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age
# print (len(Details["Student"])) 


##Q5.What would be the output of the below code snippet ?
##question5_key2
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12
# print(my_dict)
# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
# print (sum)
# print(my_dict)
# #output=30


##Q6.What would be the output of the below code snippet ?
##question6_key2
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print (len(crates['box']))
# #output=2

##Q7.What would be the output of the below code snippet ?
## question7_key2
# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"}
# id1 = id(rec)
# del rec
# rec = {"Name" : "Python","Age":"20","Addr" : "NJ", "Country" : "USA"}
# id2 = id(rec)
# print(id1 == id2)
