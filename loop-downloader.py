import os
import re
import requests
import shutil

# get data on all the magazines available
r = requests.get("https://loopwifi.co.uk/api/v2/feed?id=magazines")
magazines = r.json()[0]["channel"][0]["content"]

for magazine in magazines:
    print("Downloading " + magazine["title"] + " magazine...", end='\r')
    os.makedirs(magazine["id"], exist_ok=True)

    # get all the pages
    r = requests.get("https://loopwifi.co.uk/" + magazine["entryFile"])
    pagesUl = re.findall("<ul class=\"pageturnerCatalog\">(.*?)<\/ul>", r.text, re.DOTALL)
    pages = re.findall("<li>(.*?)</li>", str(pagesUl))
    
    pageNumber = 1
    for page in pages:
        print("Downloading " + magazine["title"] + " magazine: page " + str(pageNumber) + " of " + str(len(pages)), end='\r')
        
        # download and save the page
        url = "https://loopwifi.co.uk/magazines/magazine_assets/" + magazine["id"] + "/" + page
        r = requests.get(url, stream=True)
        with open(magazine["id"] + "/" + str(pageNumber).zfill(3) + ".jpg", "wb") as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
        pageNumber += 1

    # create a new line for the next magazine
    print()
