##Creating Daily Task App


##Function to show all the task
def ShowTask(task_list,task_status,task_DueDate):
    print()
    for i in range(len(task_list)):
        print(i+1," ",task_list[i])
        print("  Status: ",task_status[i])
        print("  Due Date: ", task_DueDate[i])

##Function to show options
def Options(task_list,task_status,task_DueDate):
    print()
    options=["Add Task","Edit task","Delete task"] 
    for i in range(len(options)):
        print(i+1,options[i]) 
    user_input=int(input("Enter option number: "))
    if user_input==1:
        AddTask(task_list,task_status,task_DueDate)
    if user_input==2:
        EditTask(task_list,task_status,task_DueDate)
    if user_input==3:
        task_list=DeleteTask(task_list,task_status,task_DueDate)

## Function to add task
def AddTask(task_list,task_status,task_DueDate):
    add_task=input("Enter task to add: ")
    task_list.append(add_task)
    add_status=input("Enter status: ")
    task_status.append(add_status)
    add_duedate=input("Enter Due Date: ")
    task_DueDate.append(add_duedate)
    print("All your tasks are: ",task_list)
    
    user_input3=input("Would you like to go back to option? enter y or n: ")
    if user_input3=="y": 
       Options(task_list,task_status,task_DueDate)
    return task_list
    return task_status
    return task_DueDate

##FUnction to Edit task
def EditTask(task_list,task_status,task_DueDate):
    print()
    print("Following are the tasks :")
    ShowTask(task_list,task_status,task_DueDate)
    print("Editing tasks....")
    print()
    user_input=int(input("Which task do you want to Edit, enter option: "))
    user_input2=input("What you want to edit status or due date: ")
    if user_input2=="status":
        Status_option=input("Enter New status: ")
        task_status[user_input-1]=Status_option
        print("Task Status Updated ")
        # print(task_status)
        user_input3=input("Would you like to go back to option? enter y or n: ")
        if user_input3=="y": 
            Options(task_list,task_status,task_DueDate)
        return task_status

    elif user_input2=="due date":
        Due_Date=input("enter new due date: ")
        task_DueDate[user_input-1]=Due_Date
        print(task_DueDate)
        return task_DueDate
        user_input3=input("Would you like to go back to option? enter y or n: ")
        if user_input3=="y": 
           Options(task_list,task_status,task_DueDate)
    

##Function to Delete task  
def DeleteTask(task_list,task_status,task_DueDate):
    print()
    ShowTask(task_list,task_status,task_DueDate)
    user_input=int(input("enter option to Delete task: "))
    del task_list[user_input-1]
    del task_status[user_input-1]
    del task_DueDate[user_input-1]
    
    user_input3=input("Would you like to go back to option? enter y or n: ")
    if user_input3=="y": 
       Options(task_list,task_status,task_DueDate)
    return task_list
    return task_status
    return task_DueDate


##Function to count the number of tasks 
def CountTask(task_list):
    count=0
    for i in task_list:
        count=count+1
    print("Now The total number of tasks are: ", count)


##Program starts
print("   Welcome to Daily Task App   ")
print()
Num_task=int(input("Enter number of tasks: "))
i=0
task_list=[]
task_status=[]
task_DueDate=[]

##creating task and task status 
while i<Num_task:
    print()
    Task=input("Enter task: ")
    Status=input("Enter task status as - Completed or Inprogress or Not started : ")
    DueDate=input("Enter Due date: ")

    task_list.append(Task)
    task_status.append(Status)
    task_DueDate.append(DueDate)
    i=i+1

ShowTask(task_list,task_status,task_DueDate)
print()
CountTask(task_list)

##Settings=Add,edit,Delete
user_input4=input("Do want to go to settings? enter y or n: ")
if user_input4=="y":
    Options(task_list,task_status,task_DueDate)
    print()

# user_input3=input("Would you like to go back to option? enter y or n: ")
# if user_input3=="y":
#    Options(task_list,task_status,task_DueDate)

print()
    
ShowTask(task_list,task_status,task_DueDate) 
print()  
CountTask(task_list)
print("Have a nice Day")  
