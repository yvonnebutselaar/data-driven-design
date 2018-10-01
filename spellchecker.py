badwords = ["broccoli", "carrots", "cauliflower", "beets", "leek", "spinach", "paksoi"]
goodwords = ["potatoes", "radishes", "courgette", "eggplant", "pumpkin", "squash", "tomatoes"]
sentencelist = input("Tell me your 2 favourite vegetables").split(" ")

index = 0
for word in sentencelist:
    if word in badwords:
        print("ERROR! You used a bad word. " + word + " should be " + goodwords[index])
    else:
        index = index + 1