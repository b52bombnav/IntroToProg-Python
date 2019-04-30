#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   Jon Vanover, 4/29/2019, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

objFile = "C:\_PythonClass\Assignment05\Todo.txt"
strData = ""
dicRow = {}
lstTable = []

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"
    
file=open(objFile,"r")  # open file to read data from

for line in file:
    strData=line.split(",")  # split the row into left and right by div at ","
    a=strData[0]  # left part of the line
    b=strData[1]  # right part of the line
    c=len(b)-1  # to remove the "\n" from the end of line find the len of the right part
    b=b[0:c]  # only copy the part of the right that does not include the "\n"
    dicRow[a]=b  # store the left and right parts together in the dict

file.close()  # close the file

lstTable = list(dicRow)  # convert the dict to a list

# Step 2 - Display a menu of choices to the user

while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    
    if (strChoice.strip() == '1'):
        print(lstTable)  # print out the list/Table       
        continue
    
    # Step 4 - Add a new item to the list/Table
    
    elif(strChoice.strip() == '2'):
        num_index = len(lstTable)+1  # find the next position in the list/Table
        new_item = input("Pleaes enter the new item for the ToDo List: ")  # prompt for item
        lstTable.insert(num_index,new_item)  # insert new_item into the list at the next index
        print("\nThe table's contents are now:",lstTable)  # print out the new table showing the insertion
        continue
    
    # Step 5 - Remove a new item to the list/Table
    
    elif(strChoice == '3'):
        print("\nThe table's contents are:",lstTable,"\n")  # print out the list/Table
        rem_item = input("Type the name of the item you want to remove: ") # prompt for the item to remove
        if rem_item in lstTable:
            lstTable.remove(rem_item)  # remove the item from the list
        else:
            print("That item is not in the list!\n")
        print("\nThe table's contents are now:",lstTable) # print out the list current state
        continue
    
    # Step 6 - Save tasks to the ToDo.txt file
    
    elif(strChoice == '4'):
        print("\nThe table's contents are:",lstTable)
        print("Saving data to file", objFile,"\n")
        file=open(objFile,"a")  # open file to append data
        file.write(str(lstTable))  # write the table to a file
        file.close()   # close the file
        continue
            
    elif (strChoice == '5'):
        break #and Exit the program

