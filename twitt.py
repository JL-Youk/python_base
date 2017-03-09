from bs4 import BeautifulSoup as soupy
import urllib, re

html = urllib.urlopen('https://twitter.com/hugo_liiine').read()
soup = soupy(html, "html.parser")

x = soup.find("meta", {"name":"description"})['content']
filter = re.findall(r'"(.*?)"',x)

tweet = filter[0]
print tweet
