# Welcome
import time
import datetime
print("Welcome to DataForMoney©, the new Social Networking experience")
time.sleep(1)

# First name
print("To register to DataForMoney©, please enter your personal details here.")
time.sleep(2)

firstname = input("Enter your first name here.")
print("Welcome, " + firstname + "!")
      
# Last name
lastname = input("Enter your last name here.")
lastname_l = lastname.lower()

if lastname_l == "butselaar":
 	print("Hello " + firstname + " " + lastname + "! A bit creepy but you have the same last name as the programmer. Maybe you guys will meet someday?")

else:
	print("Welcome " + firstname + " " + lastname + "! Don't worry, DataForMoney© is completely trustworthy. Really.")

time.sleep(2)
# Birth year check - process is in datetry.py
date = datetime.datetime.now()
currentyear = int(date.year)
currentmonth = int(date.month)
currentday = int(date.day)

yearcheck = (date.year - 18)

yearofbirth = int(input("Enter your year of birth here."))
monthofbirth = int(input("What is your birth month? Please enter two numbers (e.g. 09)"))
dayofbirth = int(input("What is your day of birth? Enter numbers 1 to 31."))

if yearofbirth < yearcheck:
	print("Thank you for your data, " + firstname + "! We promise a spam e-mail in your inbox on your birthday!")

elif yearofbirth == yearcheck:
	print("Checking month...")
	time.sleep(1)
	if monthofbirth < currentmonth:
		print("Thank you for your data, " + firstname + "! You already had your birthday this year? No discount for you, sadly.")

	elif monthofbirth == currentmonth:
		print("Checking day...")
		time.sleep(1)
		if dayofbirth < currentday:
			print("Thank you for your data, " + firstname + "! Sadly your birthday discount will have to wait until next year.")

		elif dayofbirth == currentday:
			print("Wow, happy birthday " + firstname + "! DataForMoney© has been unlocked for you today.")

		else:
			print("Sorry, you're too young to use DataForMoney©. Try again later this month, it's your birthday soon anyways. The programme is now closing...")
			exit()

	else:
		print("Sorry, you are not old enough to use our service. Try again in a few months. The service will close now.")
		exit()

else:
	print("Sorry, you are too young to register to DataForMoney© The programme will exit now.")
	exit()
time.sleep(2)

# Gender. In this part I'm assigning points to variable genderpoints, and choices you make change the value of this variable.
print ("Alright, " + firstname + ", are you male, female or other?")
time.sleep(1)
gender = input("Enter your gender here").lower()
genderpoints = int(0)

if gender == "female":
	print ("Alright, " + firstname + ". We will subscribe you to standard feminine hobbies like make-up, gossip and celeb news.")
	genderpoints = int(100)

elif gender == "male":
	print ("Hey " + firstname + "! You like football, gaming and cars, right?")
	genderpoints = int(100)

elif gender == "other":
	print ("We're not sure about your hobbies, " + firstname + ". We hope you're into knitting.")
	genderpoints = int(1000)

else:
	print ("You identify as " + gender + "? That's pretty cool, " + firstname + ". We would love to learn more about you.")
	genderpoints = int(1000)

# Last questions
time.sleep(2)
print (firstname + ", we have two last questions for you. We hope you will elaborate.")
time.sleep(1)

def relationshipcheck():
    relationshippoints = int(0)
    
    relationship = input("Are you currently in a relationship? Yes/No").lower()
    if relationship == "yes":
        print ("Wow, nice one " + firstname + "! Ask your SO to join DataForMoney© too! It's better together!")
        relationshippoints = int(1000)
    elif relationship == "no":
        print ("Too bad " + firstname + "! Maybe you'll meet someone on our platform, it's not all bots!")
        relationshippoints = int(200)
    else:
        print ("Sorry " + firstname + ". We don't know what you mean by that. Let's try again.")
        relationshipcheck()
    return relationshippoints

rpoints = relationshipcheck()

time.sleep(2)

def subscriptioncheck():
	subscription = input("Would you like to pay for our DataForMoney© Premium™ subscription? Yes/No").lower()
	if subscription == "yes":
		print ("Good choice. Don't worry, we already datamined your credit card data. It's safe with us, " + firstname + "!")
		subscriptionpoints = int(1000)
	elif subscription == "no":
		print ("We already know your credit card data anyways, " + firstname + ". Interesting Amazon purchase history.")
		subscriptionpoints = int(0)
	else:
		print ("Sorry " + firstname + ". We don't know what you mean by that. Let's try again.")
		subscriptioncheck()
	return subscriptionpoints

spoints = subscriptioncheck()

# Calculate value
birthdate = dayofbirth + monthofbirth + yearofbirth
value = birthdate + spoints + genderpoints + rpoints

print("Now calculating point value...")
time.sleep(2)
print("Congratulations, " + firstname + " " + lastname + "! You are worth " + str(value) + " points. Advertisers will love your data!")

# Goodbye statement
time.sleep(2)

print("Thank you for all your data, " + firstname + "! We won't sell it to some big, scary corporation. We promise.")
time.sleep(2)
print("Log in again soon! And remember, DataForMoney© is the best new Social Networking experience around!")
time.sleep(1)
print("Closing programme...")