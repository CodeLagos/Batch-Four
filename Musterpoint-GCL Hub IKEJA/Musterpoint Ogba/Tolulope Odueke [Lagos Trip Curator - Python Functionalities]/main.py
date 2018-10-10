#!/usr/bin/python

#Lagos Trip Curator - Python Functionalities by Tolulope Odueke (tolulope.od@gmail.com)
#A CodeLagos Project handled by Mr. Dotun - CodeLagos Facilitator MusterPoint, Ogba, Lagos.
#CodeLagos August - September, 2018.
#Please view readme.txt file for more information on this project

from crawlClass import Hotel
from weather import Weather, Unit
from time import sleep

f = open("outputfile.txt", "w")

print("Welcome to the Lagos Experience. I am an information system designed to assist your decision making process for your stay in Lagos by collecting some data from you and providing some information based on your input\n\
	Please start by telling me your name")
print()
sleep(1)

def user_name():
	name = input("What is your name? ")
	print("Hello there, ", name + ". Welcome to the Lagos Experience. Before we begin...")
	return name, "Here's a little summary based on your provided responses"

def weather_forecast():
	weather = Weather(unit=Unit.CELSIUS)
	location = weather.lookup_by_location('Ikeja')
	forecasts = location.forecast
	print("Here's a 10-day weather forcast for Lagos, Would you need an umbrella?")
	for forecast in forecasts:
		print(forecast.date,":", forecast.text)
		print("| Temp. High:",forecast.high + "℃", "| Temp. Low:",forecast.low + "℃")

def num_of_days():
	days = int(input("How many days will you be staying in lagos? "))
	return days


def users_budget():
	while True:
		try:
			users_budget = float(input("What's your budget? "))
			for amount in range(999, 100000001):
				if users_budget > amount:
					users_budget = float(users_budget)
					return users_budget
					f.write("Your budget: " + str(users_budget))
					f.close()
					break
				elif users_budget < amount:
					print(str(users_budget), " ah a challange, let's see how much fun you can have")
					return users_budget
					f.write("Your budget: " + str(users_budget))
					f.close()
					break
				else:
					print("Please enter a Valid figure!")
					break
		except ValueError:
			print("Please enter a figure")
	return float(users_budget)


def primary_transport():
	print("There are two major modes of public transport in Lagos, cabs and buses")
	modeOfTransport = int(input("What would be you primary means of movement in Lagos? (Select 1 or 2)\n\
		1. BRT Buses (BRT buses cover every area in Lagos state, are convenient and give you the full experience of being a Lagosian)\n\
		2. Cab Services (Yellow Cabs, Uber, Taxify etc. These give you a little more comfort and ease of movement, however, they may be restricted to certain areas of Lagos\n"))
	if modeOfTransport == 1:
		sleep(1)
		print("Excellent choice, you are really about to enjoy the full Lagos experience!")
		return "Your chosen Primary Mode of Transport: BRT Buses"
	elif modeOfTransport == 2:
		sleep(1)
		print("Good choice, your lagos experience always begins with your first trip!")
		return "Your chosen Primary Mode of Transport: Cab Services"
	else:
		sleep(1)
		print("You did not select any Primary Mode of Transport")
		return "Your chosen Primary Mode of Transport is unspecified"


def area_descriptions():
	#could add suggested activities here, this function would return suggested activities and places to visit in the output file
	more_info = int(input("To see some information about places you can stay and visit in Lagos enter '1' if not, enter any number to continue: "))
	if more_info == 1:
		sleep(2)
		print("Lagos is an amazing destination filled with equally amazing landmarks and a lot of activities for fun lovers. No matter where you decide to stay, you are guaranteed to have a great experience in the city that never sleeps and always holds something for the faithful.\n\
		Ikeja is the capital of Lagos state and is a well planned and quiet residential and commercial town with shopping malls, cinemas, pharmacies and government reservation areas. The Murtala Mohammed International Airport is located in Ikeja. Ikeja is also home to Femi Kuti's Africa Shrine and Lagbaja's Motherland, both venues for live music\n\
		Suggestions:\n\
		Visit Kalakuta Museum\n\
		Visit Fela's Shrine\n\
		Ndubuisi Kanu Park\n\
		Ikeja City Mall\n\
		\n\
		Lekki is located to the east of Lagos, adjoining to its west Victoria Island and Ikoyi districts of Lagos with the Atlantic Ocean to it's south. Lekki currenty houses several Estates, gated residential developments, agricultural farmlands, areas allocated for a Free Trade Zone, with an airport under construction. The peninisula is a place that's home to beautiful shorelines\n\
		Suggestions:\n\
		Lekki Conservation Centre\n\
		Eko Atlantic\n\
		Elegushi Royal Beach\n\
		Dreamworld Africana\n\
		Fun Factory\n\
		\n\
		Victoria Island is an affluent area that encompasses a former island of the same name that sits between Lagos Island and the Lekki Peninsula in the Lagos Lagoon. It is the main business and financial centre of Lagos\n\
		Suggestions:\n\
		Alpha Beach\n\
		Lekki Conservation Centre\n\
		Musical Society of Nigeria\n\
		National Museum\n\
		Red Door Gallery\n\
		\n\
		Lagos Island is the principal and central local government area in Lagos famed for its business by day and leisure by night lifestyle. It is home to numerous companies, businesses and relaxation centers\n\
		Suggestions:\n\
		Freedom Park\n\
		Tarkwa Bay Beach\n\
		Balogun Market\n\
		Oba's Palace\n\
		Tafawa Balewa Square\n\
		Tinubu Square")
		return "Suggested Activities/Places to Visit: \n\
		Visit Kalakuta Museum\n\
		Visit Fela's Shrine\n\
		Fun Factory\n\
		Red Door Gallery\n\
		Elegushi Beach\n\
		Eko Atlantic\n"
	else:
		pass
		sleep(1)
		return  "Suggested Activities/Places to Visit: \n\
		Visit Kalakuta Museum\n\
		Visit Fela's Shrine\n\
		Fun Factory\n\
		Red Door Gallery\n\
		Elegushi Beach\n\
		Eko Atlantic\n"


def area_of_residence():
	location = int(input("What area of lagos would you be staying? \n\
	1. Ikeja\n\
	2. Lekki\n\
	3. Victoria Island\n\
	4. Lagos Island\n\
	"))
	if location == 1:
		location = Hotel("Ikeja")
		location.hotel_listing('ikeja')
		sleep(1)
		print("Hotel Suggestions in Ikeja: \n ", location.hotel_listing('ikeja'))
		return location.hotel_listing('ikeja')
	elif location == 2:
		location = Hotel("Lekki")
		location.hotel_listing('lekki')
		sleep(1)
		print("Hotel Suggestions in Lekki: \n ", location.hotel_listing('Lekki'))
		return location.hotel_listing('lekki')
	elif location == 3:
		location = Hotel("Victoria Island")
		location.hotel_listing('victoria-island')
		sleep(1)
		print("Hotel Suggestions in Victoria Island: \n ", location.hotel_listing('victoria-island'))
		return location.hotel_listing('victoria-island')
	elif location == 4:
		location = Hotel("Lagos Island")
		location.hotel_listing('lagos-island')
		sleep(1)
		print("Hotel Suggestions in Lagos Island: \n ", location.hotel_listing('lagos-island'))
		return location.hotel_listing('lagos-island')
		

def message():
	print("Thank you for sharing in the Lagos Experience, I have I have been able to provide you with some useful information enough to influence your stay in the Centre of Excellence.\n\
	This little project was done by Tolulope Odueke, as a pre-requisite for the completion for the Python Development class by CodeLagos. \n\
	Every functionality is this app was built in the Python 3 programming enironment.\n\
	Thank you once again for sharing with me.\n\
	Do not forget to check the output text file that contains a summary of information based on your input in the program!\n\
	September 2018.")

f.write(str(user_name()) + "\n\n")
sleep(1)
weather_forecast()
f.write("Vacation Days: " + str(num_of_days()) +"\n\n" + "Your Trip Budget(Excl. Air or Road Fares): ₦" + str(users_budget()) + "\n\n" + str(primary_transport()) + "\n\n" + str(area_descriptions()) +"\n\n" + "Based on your selected location, Here are some hotel suggestions:\n\n" 
	+ str(area_of_residence()) + "\n\n" + "Thank you for sharing in the Lagos Experience, I have I have been able to provide you with some useful information enough to influence your stay in the Centre of Excellence." )
f.close()
sleep(1)
message()
