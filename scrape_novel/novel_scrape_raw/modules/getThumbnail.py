from bs4 import BeautifulSoup
import cloudscraper as cloudscraper
import requests as request


def getThumbnail(novelName):
    baseUrl = "https://novelfull.com/"
    bookUrl = f'https: // novelfull.com/{novelName}.html'

    scraper = cloudscraper.create_scraper()
    bookUrl = bookUrl.replace(" ", "")
    r = scraper.get(bookUrl)
    soup = BeautifulSoup(r.content, "html.parser")
    content = soup.select_one(".book img")
    mainURL = (baseUrl + str(content["src"]))
    return mainURL
