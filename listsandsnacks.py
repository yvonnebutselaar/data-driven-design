

friends = ["Donald", "Teresa", "Willem"]
snacks = []

snacks.append(input("Donald, what is your favourite snack?"))
snacks.append(input("Teresa, what is your favourite snack?"))
snacks.append(input("Willem, what is your favourite snack?"))

index = 0
for name in friends:
	snack = snacks[index]
	index = index + 1
	print (name + " likes " + snack)
