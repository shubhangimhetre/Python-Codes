print("   Welcome in cosmos ATM   ")

Card_pin=7171
Balance=60000
print("Insert your card")
language=input("enter language(english/hindi/marathi): ")
if language=="english" or language=="hindi" or language=="marathi":
    pin=int(input("enter your pin: "))
    print("Please wait.. checking your pin...")
    if pin==Card_pin:
        print("Correct pin")
        transaction=input("select transaction(Cash Withdrawl/balance enquiry/change pin): ")
        if transaction=="cash withdrawl":
            select_account=input("select account type(saving/current)")
            amount=int(input("enter amount: "))
            remaining_amount=Balance-amount
            print("Please collect your cash...")
            print("your available balance is",remaining_amount)
            user_input=input("Do you want receipt? enter y or n: ")
            if user_input=="y":
                print("collect receipt..")
                print("Transaction done")
                print("Thank you for using Cosmos ATM.")
            else:
                print("Transaction done.")
                print("Thank you for using Cosmos ATM.")
        elif transaction=="balance enquiry":
            account=input("select your account(saving/current) : ")
            print("Available balance is", Balance)
            print("thank you for using cosmos ATM")
            receipt=input("do you want receipt?(enter y or n) : ")
            if receipt=="y":
                print("collect receipt..")
                print("Thank you for using cosmos ATM")
            else:
                print("Thank you for using Cosmos ATM.")
        elif transaction=="change pin":
            newpin=int(input("please enter new pin : "))
            pin=int(input("please re-enter your pin : "))
            print("New Pin Updated..")
            print("please take your card..")
            print("Thank you for using Cosmos ATM.")
    else:
        print("wrong your pin number")
else:
    print("thank you")



