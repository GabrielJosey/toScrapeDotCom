import requests
import csv
import json

csv_columns = ["author", "typeOfQuote", "quote"]

pageNumber = 0

jsonHasContent = True

with open('toScrape.csv', 'w') as outfile:
    writer = csv.DictWriter(outfile, fieldnames = csv_columns)
    writer.writeheader()
    while jsonHasContent == True:
        pageNumber += 1
        content = requests.get('http://quotes.toscrape.com/api/quotes?page={}'.format(pageNumber)).json()
        content = content["quotes"]
        print(pageNumber)
        quotesNumber = 0
        if content != []:
            for quotes in content:
                    quotesNumber += 1
                    print(quotesNumber)
                    author = quotes["author"]["name"].encode("utf-8")
                    try:
                        typeOfQuote = quotes["tags"][0].encode("utf-8")
                    except: 
                        typeOfQuote = "Unspecified"
                    quote = quotes["text"].encode("utf-8")
                    dict = {"author": author, "typeOfQuote": typeOfQuote, "quote": quote}
                    writer.writerow(dict)
        else: 
            jsonHasContent = False
            print("All quotes scraped!")