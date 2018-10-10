import json
with open("movies.json") as f:
    movies = json.load(f)
    
ayear = input("What year do you want to see?")

for items in movies:
    if str(items["year"]) == ayear:
        print(f'{items["title"]} is a movie from {items["year"]}')
 
f.close()