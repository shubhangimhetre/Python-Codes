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
            if j=="name": #or j=="id":
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
            count=1
            c3=0
            c4=0
          
            for l in data2["course"]["exercises"]:
                # print(count,l["name"])
                # count+=1
               
                if l["parent_exercise_id"]== None:
                    c3=c3+1
                    print(c3,l["name"],"ID:",l["id"]) 
                    c4=0                                  
                elif l["id"]==l["parent_exercise_id"]:
                    c3=c3+1
                                
                    print(c3,l["name"],"ID:",l["id"])
                    c4=0
                else:
                    c4=c4+1
                    print(" ",c4,l["name"],"ID:",l["id"])
            
                  
            Ask_user2=int(input("Select course option no: "))
            c3=0
            c4=0
            m=""
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
                if n== None:
                   break
            if n!=None:
                Ask_user3=int(input("Enter subtopic option no: "))
                for l in data2["course"]["exercises"]:


                    if l["id"]==l["parent_exercise_id"]:
                        c3=c3+1
                        if Ask_user2==c3 :
                            m=l["parent_exercise_id"]
                            print(c3,l["name"],"ID:",l["id"])        
                        c4=0
                    else:
                        c4=c4+1
                        if Ask_user3==c4:
                            if m==l["parent_exercise_id"]:
                                print(" ",c4,l["name"],"ID:",l["id"])
                                print(l["content"])
               
                        
                        

                



    elif Ask_user1=="p":
        fun()
                                
fun()  


# Ask_user4=input("Enter n for next p for previous topics: ")
                # print(Ask_user4)
                # if Ask_user4=="n":
                #     print("helo")
                    # def next(c4):
                    #     c5=0
                    #     m=""
                    #     c3=0
                    #     for l in data2["course"]["exercises"]:

                    #         if l["id"]==l["parent_exercise_id"]:
                    #             c3=c3+1
                    #             if Ask_user2==c3 :
                    #                 m=l["parent_exercise_id"]
                    #         else:
                    #             c5=c5+1
                    #             if c5>c4:
                                   
                    #                 if m==l["parent_exercise_id"]:
                    #                     print(" ",c4,l["name"],"ID:",l["id"])
                    #                     print(l["content"]) 
                    # next(c4)               


                # else:       
                #     fun()