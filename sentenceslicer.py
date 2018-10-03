#input sentence
sentence = input("Enter your sentence here.")

#calculating split, splitting and printing
start = round(len(sentence) * 0.25)
end = round(len(sentence) * 0.75)

slice = sentence[start:end]
print(slice)

# sentence to list
listy = sentence.split(" ")

#splitting the list and calculating split, splitting
start_listy = round(len(listy) * 0.25)
end_listy = round(len(listy) * 0.75)

slicelist = listy[start_listy:end_listy]

#joining and printing
glue = " "
end = glue.join(slicelist)
print(end)

