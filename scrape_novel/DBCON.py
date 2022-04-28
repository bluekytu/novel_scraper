from distutils.command.install_lib import PYTHON_SOURCE_EXTENSION
import mysql.connector;
from scrapechapter import getTitleOfBook
from scrapechapter import getBlurbofBook
from scrapechapter import saveImageOfBook
from bs4 import BeautifulSoup
import cloudscraper as cloudscraper
import requests as request
scraper = cloudscraper.create_scraper()
baseUrl = "https://novelfull.com/"
bookUrl = "https://novelfull.com/ancient-strengthening-technique.html"
title = getTitleOfBook(bookUrl, scraper, BeautifulSoup)
src = saveImageOfBook(bookUrl, scraper, BeautifulSoup, baseUrl)
Blurb = getBlurbofBook(bookUrl, scraper, BeautifulSoup)
novelDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fahad1721",
    database="noveldata"
)
NovelCursor = novelDB.cursor()

sqlStatement = "INSERT INTO NOVELS (NovelName, NovelDesc, NovelImg) VALUES (%s, %s, %s)"
val = (title, Blurb, src)
NovelCursor.execute(sqlStatement, val)
novelDB.commit()
print(NovelCursor.rowcount, "record inserted. ")
