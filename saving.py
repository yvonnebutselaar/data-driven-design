#read politicians file
politicians = open("politicians.csv", "r")
list = []
#change .csv file into a list
#Assign variables to list parts and print the full sentences.
#Added index so you can see who is at what spot in the list.
index = 0
for line in politicians:
    list.append(line.split(","))
    firstname = list[index][0]
    lastname = list[index][1]
    birthyear = list[index][2]
    party = list[index][3]
    print(str(index) + ":" + firstname + " " + lastname + " was born in " + birthyear + " and a member of " + party)
    index = index + 1

print("This file has " + str(index) + " entries.")
politicians.close()

def change():
    choice = input("What do you want to do with this list? add/remove/save/quit")
    
    #adding to list by appending the entry to the list
    #So the way i'm doing it is the input is being put into a list (since we're using a list in a list.)
    #Then we append the split input to the masterlist.
    if choice == "add":
        add = input("Add your politician. Type firstname,lastname,birthyear,party")
        adl = add.split(",")
        list.append(adl)
        print("This politician has been added.")
        change()
        
    #removing by removing an entry from the list using .pop    
    elif choice == "remove":
        delindex = input("Enter the number of the politician you want to remove.") 
        index = 0
        for line in list:
            if delindex == index:
                list.remove(delindex)
                print("Number " + str(delindex) + " has been removed.")
                index = index + 1
        
            else:
                print("Error, please try again")
                change()
        
    #save to file
    #By using the * in the print statement I can print the strings to the csv file instead of the list.
    elif choice == "save":
        politicians = open("politicians.csv", "w")
        for line in list:
            s = ","
            politicians.write(s.join(line))
        politicians.close()
        print("File saved!")
        change()
        
    #Closes the programme    
    elif choice == "quit":
        print("The programme is quitting")
        exit()
        
    #To check the list
    elif choice == "print":
        print(list)
        change()
        
    #repeats the function if the input isn't recognized.
    else:
        print("Unrecognized command. Please try again.")
        change()
        
change()

