# # Q8.Tumhare pass four employes ki details hai list mai:-
# # [“neelam”,”programer”,”24”,”2400”,]
# # [“komal”,”trainer”,”24”,”20000”]
# # [“anuradha”,”HR”,”25”,”40000”]
# # [“Abhishek”,”manager”,”29”,”63000”]  
# # ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4. har ek employee ka dictionary main name,designation,age and salary honi chahiye. 
# # aur ye sab dictionary ki keys hai jismai maine list main value di hai. Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai.
# # Output:-
# #  { 
# #      "emp1":{ "name":"nilam",
# #        "Designation":"programmer",
# #        "Age":"34",
# #        "salary":"24000",
# #          }

# #     "emp2":
# #       { "name":"komal",
# #         "Designation":"Trainee",
# #         "Age":"24",
# #         "salary":"20000" ,
# #         }

 
# #     "emp3":
# #        { "name":"anuradha",
# #          "Designation":"HR",
# #          "Age":"25",
# #          "salary":"40000",
# #          }
# #     "emp4":
# #        { "name":"Abhishek",
# #          "Designation":"Manager",
# #          "Age":"29",
# #        }
# #  }


# list1=["neelam","programer","24","2400"]
# list2=["komal","trainer","24","20000"]
# list3=["anuradha","HR","25","40000"]
# list4=["Abhishek","manager","29","63000"] 
# dic={}
# d1={} 
# for i in range(len(list1)):  
#     d1["emp1"]={"Name":list1[0],"Designation":list1[1],"Age": list1[2],"Salary":list1[3]}
# dic.update(d1)

# d2={}
# for i in range(len(list2)):
#     d2["emp2"]={"name":list2[0],"Designation":list2[1],"age":list2[2],"Salary":list2[3]}
# dic.update(d2)

# d3={}
# for i in range(len(list3)):
#     d3["emp3"]={"name":list3[0],"Designation":list3[1],"age":list3[2],"Salary":list3[3]}

# dic.update(d3)

# d4={}
# for i in range(len(list3)):
#     d4["emp4"]={"name":list4[0],"Designation":list4[1],"age":list4[2],"Salary":list4[3]}
# dic.update(d4)



# print(dic)
# import json
# employee_details=open("Emp_file.json","w")
# json.dump(dic,employee_details,indent=3)
# employee_details.close()
