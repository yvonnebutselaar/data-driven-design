#read politicians file
politicians = open("politicians.csv", "r")
person = []
#change .csv file into a list
#Assign variables to list parts and print the full sentences.
#Added index so you can see who is at what spot in the list.
index = 0
for line in politicians:
    person.append(line.split(","))
    firstname = person[index][0]
    lastname = person[index][1]
    birthyear = person[index][2]
    party = person[index][3]
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
        person.append(adl)
        print("This politician has been added.")
        change()
        
    #removing by removing an entry from the list   
    elif choice == "remove": 
        num = input("Enter the number of the entry you want to remove.")
        person.pop(int(num))
        print(f"Entry {num} has been removed.")
        change()

    #save to file
    #By using the * in the print statement I can print the strings to the csv file instead of the list.
    elif choice == "save":
        politicians = open("politicians.csv", "w")
        for line in person:
            s = ","
            politicians.write(s.join(line))
        politicians.close()
        print("File saved!")
        change()
        
    #Closes the programme    
    elif choice == "quit":
        print("The programme is quitting")
        exit()
        
    #To check the list -- this is just to test the list for myself.
    elif choice == "print":
        print(person)
        change()
        
    #repeats the function if the input isn't recognized.
    else:
        print("Unrecognized command. Please try again.")
        change()
        
change()
