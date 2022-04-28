from bs4 import BeautifulSoup
import cloudscraper as cloudscraper
from scrapechapter import getContentfromChapter
from scrapechapter import getTitleofChapter
from scrapechapter import saveChapter
from scrapechapter import moveToNextPage
import re
storyURL = "https://novelfull.com/ancient-strengthening-technique.html"

scraper = cloudscraper.create_scraper()

r = scraper.get(storyURL)
soup = BeautifulSoup(r.content, "html.parser")
content = soup.select("#list-chapter li a")
link = ""
chaptersScraped = 0
pageIndex = 0
while True:
    if (chaptersScraped >= 50):
        pageIndex += 1
        print(pageIndex)
        newUrl = moveToNextPage(storyURL, scraper, BeautifulSoup, pageIndex)
        storyURL = newUrl
        print(storyURL)
        chaptersScraped = 0
        r = scraper.get(storyURL)

        soup = BeautifulSoup(r.content, "html.parser")
        content = soup.select("#list-chapter li a")


    for links in content:
        chaptersScraped += 1
        link = storyURL.replace(f"?page={pageIndex}", "").replace(".html", "") + str(links["href"]).replace("ancient-strengthening-technique/", "")
        print(link)
        chapterContent = getContentfromChapter(link, scraper, BeautifulSoup)
        title = getTitleofChapter(link, scraper, BeautifulSoup)
        print(title)
        saveChapter(title, chapterContent, re)
        print(chaptersScraped)


