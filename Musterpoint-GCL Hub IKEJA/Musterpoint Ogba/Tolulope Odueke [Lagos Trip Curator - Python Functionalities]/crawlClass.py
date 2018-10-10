import ssl
import urllib.request
from bs4 import BeautifulSoup

#create a class to handle requests as objects.
#This class opens a url specified in the body of the code and appends the
#location of the hotel search, scrapes the url for specific details which 
#in this case are the hotel names and their prices as text, which are stored in the
#HTML tags, h2 and p by parsing their classes.
#It initializes at the name of the city/state and the hotel_listing method 
#goes specifically to the area within the state the hotel is being searched for

class Hotel(object):
	"""docstring for Hotel"""
	def __init__(self, city):
		self.city = city
		#print(city)

	def hotel_listing(self, url):
		self.url = url
		link = 'https://hotels.ng/hotels-in-lagos/' + str(self.url)
		source = urllib.request.urlopen(link)
		soup = BeautifulSoup(source, 'html.parser')
		hotel_names = soup.find_all("h2", {'class' : 'listing-hotels-name' })
		hotel_prices = soup.find_all("p", {'class' : 'listing-hotels-prices-real'})
		hotels_list = []
		price_list = []
		for hotel_name in hotel_names:
			hotels_list.append(hotel_name.getText())
		for price in hotel_prices:
			price_list.append(price.getText())
		combined_list = list(zip(hotels_list, price_list))
		return combined_list

#lagos = Hotel('Here\'s some Hotels in your selected location')