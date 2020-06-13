import requests
import json

def getNames(fetch, number, f):
    #get the correct json blob
    for x in fetch.items():
        item = x

    #switch to the list of cards rather than the first part of the blob
    cardList = item[1]

    #get an individual card
    #card = cardList[0]
    #print(type(card))

    #f = open("cardnames.txt", "a+")

    for card in cardList:
        f.write(str(number))
        f.write(' ')
        f.write(card['name'])
        f.write('\n')


f = open("cardnames.txt", "w+")


response = requests.get("https://api.scryfall.com/cards/search?order=cmc&q=set%3Adom+rarity%3Am")
fetch = response.json()

number = int(input("How many copies do you want of each Mythic?"))
f.write('Mythics \n')
getNames(fetch, number, f)
f.write('\n')
print()

response = requests.get("https://api.scryfall.com/cards/search?order=cmc&q=set%3Adom+rarity%3Ar")
fetch = response.json()

number = int(input("How many copies do you want of each Rare?"))
f.write('Rares \n')
getNames(fetch, number, f)
f.write('\n')
print()

response = requests.get("https://api.scryfall.com/cards/search?order=cmc&q=set%3Adom+rarity%3Au")
fetch = response.json()

number = int(input("How many copies do you want of each Uncommon?"))
f.write('Uncommons \n')
getNames(fetch, number, f)
f.write('\n')
print()

response = requests.get("https://api.scryfall.com/cards/search?order=cmc&q=set%3Adom+rarity%3Ac")
fetch = response.json()

number = int(input("How many copies do you want of each Common?"))
f.write('Commons \n')
getNames(fetch, number, f)
f.write('\n')
print()

f.close()









