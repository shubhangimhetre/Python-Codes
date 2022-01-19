##Ola-Uber 
print(" ")
print("HELLO!! WELCOME TO ROYAL TRAVELLERS🙏")
print(" ")

def Vehicles():
    vehicle=["Bike🏍","Auto🛺","Car mini🚗","Car Prime🚙"]
    vehicle_no=["MH12 4345","MH12 4567","MH12 4879","MH12 8976"]
    colour=["Blue","Black","Red","White"]
    print("vehicles: ")
    for i in range(len(vehicle)):
        print(i+1," ", vehicle[i])
        print("   Vehicle number: ",vehicle_no[i])
        print("   Vehicle's colour: ", colour[i])
    select_vehicles=int(input("Select vehicle option: "))
    return select_vehicles

def Drivers():
    print(" ")
    Name=["Ajay👮","Bipin👮","Chetan👮","Dnyanesh👮"]
    Phone=[9878127656,8798657687,8798656754,7685323120]
    Rating=[7,8,7,9]

    for i in range(len(Name)):
       print( i+1,"Driver name: ", Name[i])
       print("   Phone number📞: ",Phone[i])
       print("   Rating of Driver⭐️: ",Rating[i])
    select_driver=input("   Enter driver option: ")
    
    
def fare(km,vehicle_option):
    Rate=[8,10,11,15]
    print("Your selected vehicles rate per km is: ",Rate[vehicle_option-1])
    fare=km*Rate[vehicle_option-1]

    print("Your total fare is Rs: ", fare)
    print(" ")
    Earning=[0,0,0,0]
    Earning.insert(vehicle_option-1,fare)


def payment():
    payment=["cash💵","UPI💳"]
    print("Payment modes: ")
    for i in range(len(payment)):
        print(i+1," ",payment[i]) 
    option=int(input("Enter payment option: "))
    payment_mode=payment[option-1]
    return payment_mode
   
current_location=input("enter your current location: ")
dropping_point=input("enter your dropping point: ")

vehicle_option=Vehicles()
Drivers()

import random
km=random.randint(1,50)
print(" ")
print("Your location distance in km is: " ,km)
fare(km,vehicle_option)

confirmation=input("Confirm your booking enter y or n : ")
if confirmation=="y":
    import random
    otp=random.randint(1000,2000)
    print(" ")
    print("Your otp is: ",otp)
    print("share it with Driver")
    print(" ")
    cancellation=input("Do you want to cancel ride enter y or n: ")
    if cancellation=="n":
        payment_mode=payment()
        print("Your payment mode is: ", payment_mode)
        transaction=input("Transaction done? Enter y or n : ")
        if transaction=="y":
            print("Ok done👍!!")  
            print(" ")
            feedback=int(input("enter rating from 1 to 10: "))
            Rating=[7,8,7,9]
            New_rating=(Rating[vehicle_option-1]+feedback)/2
            Rating.insert(vehicle_option-1,New_rating)
            print("Drivers new Rating is: ",New_rating)
            print(" ")
            print("Thank you🙏, visit again")
        else:
            print("Not done, try again.")            
    else:
        print("Thank you for visiting our app🙏, bye bye")
else:
    print("Thank you for visiting our app🙏, bye bye")
    # aap jab car prime,cab aur chize jo dikha rho usme driver ki details mt dikhao
    # jb driver ki details dikha rhe ho toh price,carnumber,feedback,typeofcar,colour of car,kaha pr driver hai,kitna time lagega driver ko ane me,
    # distance dikhao
    # otp confirm karo user se
    # last me feedback lo
