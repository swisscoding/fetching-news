#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
#
# Prerequierities:
# Get your own API key -> https://newsapi.org/

from colored import stylize, fg
import requests

# decoration
print(stylize("\n---- | Fetching news from BBC | ----\n", fg("red")))

# class
class News:
    def __init__(self, key):
        self.key = key

    # output magic method
    def __repr__(self):
        counter = 1
        for headline in self.get_news(self.key):
            print(f"{str(counter)}. {headline}")
            counter += 1

        return ""

    # methods
    def get_news(self, key):
        # You can change this url on https://newsapi.org/
        url = f"http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={key}"

        contents = requests.get(url).json()
        articles = contents["articles"]
        headlines = []

        for a in articles:
            if len(headlines) == 5:
                break

            headlines.append(a["title"])

        return headlines

# main execution
if __name__ == "__main__":
    # user interaction
    api_key = input("Your API key: ")
    print()

    print(News(api_key))
