# Write a program to print 'exists' if entered key already exists in the dictionary and print 'not exists' if the entered key does not exist.
# Example :-


dict={"name":"Raju","Marks":56}
Input_key=input("enter a key to check: ")
if Input_key in dict:
    print("Yes, Your entered key Exists in dict")
else:
    print("No, your entered key Not Exists in dict")