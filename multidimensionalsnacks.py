friends = [
    ["Donald"],
    ["Teresa"],
    ["Willem"],
        ]

for friend in friends:
    name = friend[0]
    namelen = len(name)
    print (name + " is a " + str(namelen) + " letter word")

for friend in friends:
    name = friend[0]
    friend.append(input(name + " what is your favourite snack?"))
    
for friend in friends:
    name = friend[0]
    snack = friend[1]
    print (name + " likes " + snack)