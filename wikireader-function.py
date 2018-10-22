import requests
import json

#Ask user what they want to read
title = input("What do you want to read about?").strip().replace(" ","_")
value = input("Would you like the description or extract? Enter description or extract.").strip().lower()
printurl = input("Would you like to print the URL? yes/no").strip().lower()



#Function 1: API call. After this function I use req as a variable to use it in our second function.
def getwiki(title, value):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    req = requests.get(url)
    return req
    
req = getwiki(title, value)

#Function 2: Return Info. Changes the outcome from function 1 into useable data. 
def retinfo():
    dat = json.loads(req.text)
    return dat[value]
    
data = retinfo()

#Calling the functions!
getwiki(title, value)
retinfo()

#Printing our results.
print(f"The {value} of {title} is as follows:")
print(data)

#To get the desktop url I've added another function.
def printy():
    dat = json.loads(req.text)
    return dat["content_urls"]["desktop"]["page"]

desktop_url = printy()

#But we only want to run this if printurl=yes.
if printurl == "yes":
    printy()
    print(f"The desktop URL is {desktop_url}.")
    
else:
    print("You did not request the URL.")
