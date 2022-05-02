import os
from os.path import isdir


def getContentfromChapter(url, scraper, BeautifulSoup):
    r = scraper.get(url)

    soup = BeautifulSoup(r.content, "html.parser")
    content = soup.select("#chapter-content p")
    realContent = ""
    for contents in content:
        realContent += contents.text.strip() + " \n \n"
    return realContent


pass


def getTitleofChapter(url, scraper, BeautifulSoup):
    r = scraper.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    content = soup.select_one(".chapter-title span")
    if content is not None:
        return content.text.strip()
    else:
        pass


def saveChapter(name, content, re):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    fname = str(name).replace(":", "") + ".txt"
    fnamenew = re.sub('[@_!#$%^&*()<>?/\|}{~:]','',fname)
    dir = "../Novel_Data/NOVELS/ancient-strengthening-technique/"
    if isdir(dir) is not True:
        os.mkdir(dir)
    else:
        print("exists")

    fnamenew = dir + fnamenew
    with open(fnamenew, "w", encoding="utf-8") as f:
        f.write(str(content))


pass


def moveToNextPage(CurrentUrl, scraper, BeautifulSoup, PageIndex):
    UrlToMoveTo = ""
    if str(CurrentUrl).endswith(".html"):
        UrlToMoveTo = CurrentUrl + f"?page={PageIndex}"
    elif "?page=" in str(CurrentUrl):
        UrlToMoveTo = str(CurrentUrl).replace(f"?page={PageIndex - 1}", f"?page={PageIndex}")

    return UrlToMoveTo


pass

def saveImageOfBook(StoryUrl, scraper, BeautifulSoup, baseUrl):
    r = scraper.get(StoryUrl)
    soup = BeautifulSoup(r.content, "html.parser")
    content = soup.select_one(".book img")

    return baseUrl + str(content["src"])

def getTitleOfBook(baseURL, scraper, BeautifulSoup):
    r = scraper.get(baseURL)
    soup = BeautifulSoup(r.content, "html.parser")
    content = soup.select_one(".title")
    return content.text.strip()

def getBlurbofBook(BookUrl, scraper, BeautifulSoup):
    r = scraper.get(BookUrl)
    soup = BeautifulSoup(r.content, "html.parser")
    content = soup.select(".desc-text")
    realContent = ""
    for paragraphs in content:
        realContent += str(paragraphs.text.strip()) + "\n"
    return realContent

def saveBlurb(title, blurb):
    with open(f"../Novel_Data/NOVEL_BLURBS/{title} BLURB.txt", 'w') as f:
        f.write(blurb)


