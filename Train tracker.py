from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

tref_url = "https://www.thetrainline.com/train-times/penarth-to-trefforest-station"

pen_Url = "https://www.thetrainline.com/train-times/trefforest-station-to-penarth/31-oct-2017/0015"

def chooseClient(): #Set the URL that will be scanned
    choice = raw_input("To p or t?:\n")
    if choice == "p":
        client = uReq(pen_Url)
    elif choice == "t":
        client = uReq(tref_url)
    return client

client = chooseClient()

htmlPage = client.read()

client.close() #closes the page

#parses the html code for access
page_soup = soup(htmlPage, "html.parser")


starting = page_soup.findAll("div", {"class": "row origin"})
for times in starting:
    startlocation = page_soup.findAll("div", {"class": "row origin"})
    baseStation = startlocation[0].text.strip()

#Output
count = 0
for num in startlocation:
    print startlocation[count].text.replace(" ","").strip() + "\n _____________________________________________________"
    count = count + 1
