
'''
Write a program to store the stock information of a departmental store. Information should be name, price, quantity
and type of item. Use while loop to take the input untiluser wants. You need to write those information in a file.
After the user inputs data, display information for specific item by reading the file written in first step.
Use file handling with proper exception handling. You may use data structures if you want.
Please​ ​use​ ​delimiters​ ​like​ ​​;​​ ​or​ ​​|​ ​​to​ ​separate​ ​the​ ​data​ ​values.

'''

fp = open("department_stockinfo.txt","a+")
fp.write("\t\tName|\t\tPrice|\t\tQuantity|\t\tItem type|\n")

def fileWrite(name , price,quantity, item_type):
    fp.write("\t" + (name) + "|\t")
    fp.write("\t" + (price) + "|\t")
    fp.write("\t" + (quantity) + "|\t")
    fp.write("\t" + (item_type) + "|\n")

choice = 'y'

while choice == 'y': #Take the input until user wants
    name = input("Enter the Name of product:\n")
    price = input("Enter Price of product:\n")
    quantity = input("Enter the Quantity:\n")
    item_type = input("Enter the Item type:\n")

    fileWrite(name, price, quantity, item_type)

    choice = input('Enter your choice y to enter details or n to exit:')
    if(choice == 'n'): #To exit
        break

fp.close() #closing file
fp = open("department_stockinfo.txt","r") #open file in read mode
a = fp.read()
for i in a:
    print(i)
    fp.close()