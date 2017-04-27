import requests
from bs4 import BeautifulSoup

def getLawxpData():
    query='http://www.lawxp.com/statute/?RegionId=100000&q=%E5%A4%A7%E6%B0%94&pg=2'
    page = requests.get(query)
    soup = BeautifulSoup(page.content)
    print(soup.select("div[class=xfg-news1]"))



if __name__=='__main__':
    getLawxpData()
