import shutil

from scrapechapter import saveImageOfBook

from bs4 import BeautifulSoup
import cloudscraper as cloudscraper
import requests as request
from scrapechapter import getTitleOfBook
from scrapechapter import getBlurbofBook
from scrapechapter import saveBlurb
import wget as wget

scraper = cloudscraper.create_scraper()
baseUrl = "https://novelfull.com/"
bookUrl = "https://novelfull.com/ancient-strengthening-technique.html"
src = saveImageOfBook(bookUrl, scraper, BeautifulSoup, baseUrl)
title = getTitleOfBook(bookUrl, scraper, BeautifulSoup)
Blurb = getBlurbofBook(bookUrl, scraper, BeautifulSoup)
saveBlurb(title, Blurb)
headers = {
    'Mozilla/5.0 (X11; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0'
}
r = request.get(src, stream=True)
if r.status_code == 200:
    with open(f"../Novel_Data/NOVEL_THUMBNAILS/{title}.png", 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
