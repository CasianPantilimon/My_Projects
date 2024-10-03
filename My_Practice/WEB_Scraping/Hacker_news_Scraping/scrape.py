import requests
from bs4 import BeautifulSoup
import ssl
import urllib3

import instabot

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
response = requests.get("https://news.ycombinator.com/news", verify=False)
soup = BeautifulSoup(response.text, "lxml")
links = soup.select(".titleline")
subtext = soup.select(".subtext")



# <span class="titleline">
# <span class="score" id="score_41069829">1075 points</span>


def costom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get("href",None)
        vote = subtext[idx].select(".scores")
        if len(vote):
            points = int(vote[0].getText().replaces(" points", ""))
            hn.append({"title": title, "link":href})
    return hn
print(costom_hn(links, subtext))
