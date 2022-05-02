from bs4 import BeautifulSoup
import cloudscraper as cloudscraper


def getThumbail(novelName):
    baseUrl = "https://novelfull.com/"
    bookUrl = f'https: // novelfull.com/{novelName}.html'
