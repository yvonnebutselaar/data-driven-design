snackfriends = {
        "Donald" : "",
        "Teresa" : "",
        "Willem" : ""
        }

for key in snackfriends:
    snackfriends[key] = input(f"enter {key}'s snack here.")  
    val = snackfriends[key]

for key, val in snackfriends.items():
    print(f"{key} likes {val}.")