#read politicians file
politicians = open("politicians.csv", "w")

#change .csv file into a list
#Assign variables to list parts and print the full sentences.
#Added index so you can see who is at what spot in the list.
index = 0
for line in politicians:
    list = line.split(",")
    firstname = list[0]
    lastname = list[1]
    birthyear = list[2]
    party = list[3][:-1]
    print(str(index) + ":" + firstname + " " + lastname + " was born in " + birthyear + " and a member of the " + party + ".")
    index = index + 1

#Function to make changes to the list. I chose a function to make it repeatable, so users put in the right commands.)
def chooseyouraction():
    choice = input("What do you want to do with this list? remove/add/save/quit")
    #Remove: Removes list part based on index number.
    if choice == "remove":
        index = 0
        print("Type the index number of the politician who you would like to remove.")
        remove = input("Enter your number here.")
        for line in politicians:
            list.pop(remove)
            print("Line " + remove + " has been succesfully removed.")
            index = index + 1
        chooseyouraction()
    
    elif choice == "add":
        print("Who do you want to add to the list?")
        adding = input("Enter first name, last name, birthyear and party. Seperate with commas. /n For instance Mark,Rutte,1967,VVD").split(",")
        list.append(adding)
        print("Your addition has been added to the list.")
        chooseyouraction()
    
    elif choice == "save":
        print("The programme will now save your changes.")
            
        for line in politicians:
            politicians.write(line)
            index = index + 1   
        chooseyouraction()             
    
    elif choice == "quit":
        print("The programme will now exit.")
        exit()
    
    else:
        print("Unrecognized command. Please try again.")
        chooseyouraction()
        
chooseyouraction()
    
politicians.close()
