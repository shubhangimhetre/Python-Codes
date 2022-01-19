import json
import os
list1=[]
dic={}

def LoginSignup():
    def password_val(Password):
        len_pw=len(Password)
        if len_pw<=6:
           print("Password should have length minimum 6.")
        spl='!@#$%^&*()-+'
        l=[0,0,0,0]
        for i in Password:
            if i.isdigit(): 
               l[0]=1
            elif i.isupper():
                l[1]=1
            elif i.islower():
                l[2]=1
            elif i in spl:
                l[3]=1               
        if sum(l)==4:
            pw1=True
        else:
            print("Password should contain atleast one uppercase, lowercase ,one special character and one number.")
        if pw1==True:
            pw2=input("enter Confirm password: ")
            if Password==pw2:
               pw_vald=True
               print(pw_vald)
               return pw_vald
            else:
                print("Both password are not same,Try again")
                LoginSignup()
                
    
    Path_Exists=os.path.exists("Userdetails1.json")
    # print(Path_Exists)
    User_input=input("login or signup: ")
    
    if User_input=="signup":
        if Path_Exists==False:
            d1={} 
            d2={}   
            Username=input("Enter username: ")   
            Password=input("Enter password: ")
            pw_vald=password_val(Password)
            if pw_vald==True:    
                d1["Username"]=Username
                d1["Password"]=Password 
                print("Congrats,", Username,"You are signed up successfully..") 
                Description=input("enter your description: ") 
                Birthdate=input("Birthdate: ")  
                Hobbies=input("Hobbies: ") 
                Gender=input("Gender: ") 
                d2["Description: "]=Description
                d2["Birthdate: "]=Birthdate
                d2["Hobbies: "]=Hobbies
                d2["Gender"]=Gender
                d1["Profile"]=d2
                dic[Password]=d1                      
                with open("Userdetails1.json","w") as f1:
                    json.dump(dic,f1, indent=3)         
        elif Path_Exists==True: 
            d1={}
            d2={}
            Username=input("Enter username: ")   
            Password=input("Enter password: ")
            pw_vald=password_val(Password)
            if pw_vald==True:  
                d1["Username"]=Username
                d1["Password"]=Password 
                print("Congrats,", Username,"You are signed up successfully..") 
                Description=input("enter your description: ") 
                Birthdate=input("Birthdate: ")  
                Hobbies=input("Hobbies: ") 
                Gender=input("Gender: ") 
                d2["Description: "]=Description
                d2["Birthdate: "]=Birthdate
                d2["Hobbies: "]=Hobbies
                d2["Gender"]=Gender
                d1["Profile"]=d2
                with open("Userdetails1.json","r") as f:
                    main_dic=json.load(f)                    
                    main_dic[Password]=d1
                with open("Userdetails1.json","w") as f1:
                    json.dump(main_dic,f1,indent=3)  
        else:
            print("Error1") 

    elif User_input=="login":
        Username=input("Enter username: ")   
        Password=input("Enter password: ")
        pw_vald=password_val(Password)
        if pw_vald==True: 
            with open("Userdetails1.json","r") as f2:
                data=json.load(f2) 
            for i in data.keys():
                # print(i)
                if Password==i:
                    for j in data[i]:                           
                        # print(data[i]["Username"])
                        if data[i]["Username"]==Username:
                            print("Congrats,",Username,"You logged in successfully..")
                            break                        
                        else:
                            print("This Username is not registered, you have to signup for new registration.")
                            LoginSignup()
                    break
                else:
                    print("you have to signup for new registration.")
                    LoginSignup() 
    else:
        print("ERROR, You entered wrong input, Try again ")
        LoginSignup()
    
LoginSignup()



    