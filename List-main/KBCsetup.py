list1=["How many continents are there?", "What is the capital of India?","NG mei kaun se course padhaya jata hai?"]
soln=[3,4,1]
options=[["four","nine","seven","eight"],["chandigarh","Bhopal","chennai","Delhi"],["Software engineering","Counseling","tourism","Agriculture"]]
i=0
c=0
while i<len(list1):
    if i==0:
        print(list1[i])
        j=0 
        print("Your Options are: ")
        while j<len(options[i]):
            print(j+1,". ",options[i][j])
            j=j+1
        s1=int(input("Enter option no: "))
        if s1==i+3:
            print("Congratulations! option 3 is correct Answer")
        elif s1!=i+3:
            print("Sadly,your answer is not correct")
            n=input("You are out of the game, do you want to use 50-50 lifeline? enter y or n")
            if n=="y":
                c=c+1
                print(list1[i])
                j=0
                print("Your Options are: ")
                while j<len(options[i]):
                    print(j+1,". ",options[i][j])
                    j=j+1
                s1=int(input("Enter option no: "))
                s2=int(input("Enter your second option: "))
                if s1==i+3 or s2==i+3:
                    print("Congratulations! option 3 correct Answer")
                else:
                    print("Sorry, your answer is not correct, you missed the 50-50 lifeline")    
    elif i==1:
        print(list1[i])
        j=0 
        print("Your Options are: ")
        while j<len(options[i]):
            print(j+1,". ",options[i][j])
            j=j+1
        s1=int(input("Enter option no: "))
        if s1==i+3:
            print("Congratulations! option 4 is correct Answer")
        elif s1!=i+3:
            print("Sadly,your answer is not correct,You are out of the game,")
            if c==0:
                n=input("You are out of the game, do you want to use 50-50 lifeline? enter y or n")
                if n=="y":
                    c=c+1
                    print(list1[i])
                    j=0
                    print("Your Options are: ")
                    while j<len(options[i]):
                        print(j+1,". ",options[i][j])
                        j=j+1
                    s1=int(input("Enter option no: "))
                    s2=int(input("Enter your second option"))
                    if s1==i+3 or s2==i+3:
                        print("Congratulations! option 4 is correct Answer")
                    else:
                        print("Sorry, your answer is not correct, you missed the 50-50 lifeline")        
            else:
                print("Sorry,You already used 50-50 Lifeline,You are out of the game.Goodbye")
                break
    elif i==2:
        print(list1[i])
        j=0 
        print("Your Options are: ")
        while j<len(options[i]):
               print(j+1,". ",options[i][j])
               j=j+1
        s1=int(input("Enter option no: "))
        if s1==i-1:
            print("Congratulations! option 1 is correct Answer")
        elif s1!=i-1:
            print("Sadly,your answer is not correct,You are out of the game,")
            if c==0:
                n=input("You are out of the game, do you want to use 50-50 lifeline? enter y or n")
                if n=="y":
                    c=c+1
                    print(list1[i])
                    j=0
                    print("Your Options are: ")
                    while j<len(options[i]):
                        print(j+1,". ",options[i][j])
                        j=j+1
                    s1=int(input("Enter option no: "))
                    s2=int(input("Enter your second option"))
                    if s1==i-1 or s2==i-1:
                        print("Congratulations! option 1 is correct Answer")
                    else:
                            print("Sorry, your answer is not correct, you missed the 50-50 lifeline")        
            else:
                print("Sorry,You already used 50-50 Lifeline,You are out of the game.Goodbye")
    i=i+1
