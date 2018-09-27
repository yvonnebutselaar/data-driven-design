# names
nameone = input("Enter your name").lower().strip()
nametwo = input("Enter your lovers' name").lower().strip()

# length of names
if len(nameone) == len(nametwo):
    print("You guys fit perfectly together!")
    
elif len(nameone) < len(nametwo):
    print("Oh no, " + nameone + " is keeping secrets!")
    
else:
    print("Watch out for " + nametwo + "'s bad side'")