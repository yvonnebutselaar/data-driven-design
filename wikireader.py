import requests
import json

from IPython.display import display, Image

#Name all info we need
art = input("What article do you want to read?").replace(" ", "_")
url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{art}"
req = requests.get(url)
data = json.loads(req.text)
status = req.status_code

#Variables for our headers
title = data["title"]
desc = data["description"]
extr = data["extract"]
thumb = data["originalimage"]["source"]
img = Image(url = thumb)

if status == 200:
    print("Website is online! We'll proceed!")
    
    print("Title:", title)
    print("Description:", desc)
    print("Extract:", extr)
    print("Image:")
    display(img)
    
else:
    print("Error! We're receiving an error " + str(status))
    


