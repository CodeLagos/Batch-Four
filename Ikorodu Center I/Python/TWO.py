_author_  = "olumide maleem"

# OLUMIDE BELLO
# DATE = 2018/09/02
# CODE-LAGOS-PROJECT


import requests
from bs4 import BeautifulSoup

print("PLEASE NOTE \n USE HYPNEN (-) IN PLACE OF SPACEBAR WHEN INPUTING NAMES ")
print("EXAMPLES ARE \n RICK-ROSS \n DICED-PINEAPPLES \n ")
"""
this programm takes data from a website (GENIUS LYRICS)\
a popular lyrics site and prints the data or tests of the \
lyrics that was requested for
we need the artistes name and the songs name \
instructions are IMPORTANT as well
"""

# https://genius.com/Rick-ross-diced-pineapples-lyrics

songs_name = input("input the name of the song : ") #name of the song
artiste_name = input("input the name of the artiste : ")#name of the artiste
half_url = "https://genius.com/" #some part of the url
end = "-lyrics" #some other part

full_url = half_url + artiste_name + "-"+songs_name+ end # full valid url

#request to get data from the url
r = requests.get(full_url)

#content of the url
data = r.content

#beautiful soup function
soup = BeautifulSoup(data, "html.parser")

# finds lyrics text with the html tags which contain the data
element = soup.find("div", {"class": "lyrics"})

print("\n")   #newline
print("\n")   #newline

print(element.text.strip())

print("\n")

# https://genius.com/Rick-ross-diced-pineapples-lyrics
# https://genius.com/Rick-ross-diced-pineapples-lyrics

