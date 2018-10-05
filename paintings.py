paintings = open("paintings.csv")  

newfile = open("paintings_two.csv", "w")

for line in paintings:
    list = line.split(",")
    name = list[0]
    artist = list[1]
    price = list[2] 
    print(name + " is a painting by " + artist + " and was sold for " + price + " million dollars.")
    newfile.write(name + " is a painting by " + artist + " and was sold for " + price + " million dollars. \n") 
    
newfile.close()
paintings.close()