##Request question one
import requests
import json
from requests.api import request

# import os
# r=requests.get("https://api.merakilearn.org/courses")
# # print(r)
# a = r.json()
# # print(a)

# with open("courses1.json","w") as f:
#     json.dump(a,f,indent=4)
def fun():
    with open("courses1.json","r") as file1:
        data=json.load(file1)
    c=0
    for i in data:
        for j in i:
            if j=="name": 
                c=c+1
                print(c,i["name"],"ID:",i["id"])
    course_details=int(input("Select the course option number you want? : "))
    
    print("You selected course: ")
    print(data[course_details-1]["name"])
    user1=data[course_details-1]["id"]

    Ask_user1=input("Please enter n for next page and p for previous page: ")  
    if  Ask_user1=="n":
        r2=requests.get("https://api.merakilearn.org/courses/"+str(user1)+"/exercises")
        # print(r2)
        b=r2.json()
        # print(b)
        with open("Course_data.json","w") as f2:
            json.dump(b,f2,indent=4)
        with open("Course_data.json","r") as f3:
            x=f3.read()
            data2=json.loads(x)
            def fun3(data2):
                c3=0
                c4=0
               
                m=""
                for l in data2["course"]["exercises"]:


                    if l["parent_exercise_id"]== None:
                        c3=c3+1
                        print(c3,l["name"],"ID:",l["id"]) 
                        c4=0                                  
                    elif l["id"]==l["parent_exercise_id"]:
                        c3=c3+1
                        m=l["parent_exercise_id"] 
                        print(c3,l["name"],"ID:",l["id"])
                        c4=0
                    else:
                        c4=c4+1
                        if m==l["parent_exercise_id"]:
                            print(" ",c4,l["name"],"ID:",l["id"])
            fun3(data2) 

            Ask_user2=int(input("Select course option no: "))
            c3=0
            c4=0
            m=""
            list1=[]
            n=""
            for l in data2["course"]["exercises"]:
                
                if l["parent_exercise_id"]== None:
                    c3=c3+1
                    if Ask_user2==c3:
                        n=l["parent_exercise_id"]
                        print(c3,l["name"],"ID:",l["id"])
                        print(l["content"]) 
                        break
                    c4=0                                  
                elif l["id"]==l["parent_exercise_id"]:
                    c3=c3+1
                    
                    if Ask_user2==c3 :
                        m=l["parent_exercise_id"]
                        print(c3,l["name"],"ID:",l["id"])
                        
                    c4=0
                else:
                    c4=c4+1
                    if m==l["parent_exercise_id"]:
                        print(" ",c4,l["name"],"ID:",l["id"])
                        list1.append(l["name"])
        # print(list1)
        if len(list1)>1:      
            Ask_user3=int(input("Select subtopic option no: "))
            def fun2(Ask_user3):
                for l in data2["course"]["exercises"]:
                    # for i in range(len(list1)):
                    if m==l["parent_exercise_id"]:
                        if l["name"]==list1[Ask_user3-1]:
                            print( Ask_user3,l["name"]," ", l['id'])
                            print(l["content"])
                            if Ask_user3<=len(list1)-1:
                                user_input2=input("enter n for next and p for previous: ")
                                if user_input2=="n":
                                    Ask_user3+=1
                                    fun2(Ask_user3)                               
                                else:
                                    fun()
                            else:
                                 print("end page.")
                            break                   
            fun2(Ask_user3)            
        else:
            print("End page.")

    elif Ask_user1=="p":
        fun()
                                
fun()