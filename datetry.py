# Below is my first try. So this obviously doesn't work since currentyear is always 2018 (or whatever it is on your system right now.) 
# We could do something importing the date and subtract 18 from it so you always check whether the person is 18 or not).
# Even though this is a fail I wanted to keep it because it's fun.
import datetime
date = datetime.datetime.now()
currentyear = str(date.year)
currentmonth = str(date.month)

yearofbirth = input("Enter your year of birth here.")
monthofbirth = input("What is your birth month? Please enter two numbers (e.g. 09)")

if yearofbirth <= currentyear:
	print("Sorry, you are too young to register to DataForMoney©.")

elif (yearofbirth == currentyear) + (monthofbirth == currentmonth):
	print("Sorry, we can't guarantee that you're old enough to use our service. Try again in a month.")

else:
	print("Thank you for your data, " + firstname + "! We promise a spam e-mail in your inbox when your birthday rolls around.")


# Second try
import datetime
date = datetime.datetime.now()
currentyear = int(date.year)
currentmonth = int(date.month)
currentday = int(date.day)

yearcheck = str((date.year - 18))

firstname = input("What's your name?")
# adding the first name allows me to test this in jupyter.

yearofbirth = input("In what year were you born?")
monthofbirth = int(input("What is your birth month?"))
dayofbirth = int(input("What is your day of birth? Enter numbers 1 to 31."))

if yearofbirth < yearcheck:
	print("Thank you for your data, " + firstname + "! We promise a spam e-mail in your inbox when your birthday rolls around.")

elif (yearofbirth == yearcheck):
	print("Checking month...")
	time.sleep(2)
	if (monthofbirth < currentmonth):
		print("Thank you for your data, " + firstname + "! Too bad your birthday already happened this year. No birthday discounts for now.")

	elif (monthofbirth == currentmonth):
		print("Checking day...")
		time.sleep(2)
		if (dayofbirth <= currentday):
			print("Thank you for your data, " + firstname + "! We promise a spam e-mail in your inbox when your birthday rolls around.")

		else:
			print("Sorry, you're too young to use DataForMoney©. Try again later, it's your birthday soon anyways.")
	else:
		print("Sorry, we can't guarantee that you're old enough to use our service. Try again in a month.")

else:
	print("Sorry, you are too young to register to DataForMoney©.")

