snackfriends = {
        "Donald" : "",
        "Teresa" : "",
        "Willem" : ""
        }

snackfriends["Donald"] = input("Enter Donald's snack here.")
snackfriends["Teresa"] = input("Enter Teresa's snack here.")
snackfriends["Willem"] = input("Enter Willem's snack here.")

for key in snackfriends:
    val = snackfriends[key]
    print(key + " likes " + val)
    