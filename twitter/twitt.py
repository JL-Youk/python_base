import urllib, re
from bs4 import BeautifulSoup as soupy

html = urllib.urlopen('https://twitter.com/KittingKitten').read()
soup = soupy(html, "html.parser")

x = soup.find("meta", {"name":"description"})['content']
filter = re.findall(r'"(.*?)"',x)

tweet = filter[0]
print tweet
