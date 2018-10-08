#Define dictionary
favmovie = {
    "name" : "The Lord of the Rings: Return of the King",
    "year" : 2003,
    "duration" : 201,
    "director" : "Peter Jackson"
}

#adding actors
favmovie["actors"] = ["Elijah Wood", "Sean Astin", "Viggo Mortensen", "Ian McKellen"]
    
#for loop to print the values
for key in favmovie:
    value = favmovie[key]
 
    if key == "duration":
        print(f'{key}: {value} minutes')
        
    elif key == "actors":
        g = ", "
        print(key + ": " + g.join(favmovie["actors"]))
        
    else:
        print(f"{key}: {value}")