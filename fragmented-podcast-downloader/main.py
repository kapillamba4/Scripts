import requests
import urllib3
import os
from bs4 import BeautifulSoup

def get_download_link(episode_url):
    response = urllib3.PoolManager().request("GET", episode_url)
    soup = BeautifulSoup(response.data, "html.parser")
    for elem in soup(text="Download"):
        print("Downloading %s from %s" % (episode_url, elem.parent.get("href")))
        os.system("wget --directory-prefix=%s -c %s" % ("./fragmented-podcast", elem.parent.get("href")))

base_url = "http://fragmentedpodcast.com/episodes/all/"
http = urllib3.PoolManager()
response = http.request("GET", base_url)
soup = BeautifulSoup(response.data, "html.parser")
episodes_urls = soup.findAll(class_="w4pl_post_title")
for episode in episodes_urls:
    url = episode.get("href") 
    if url != "http://fragmentedpodcast.com/episodes/effective-java/" and url != "http://fragmentedpodcast.com/episodes/all/":  
        #print(url)
        get_download_link(url)
