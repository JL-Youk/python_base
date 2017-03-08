import urllib, os, sys
import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen('https://twitter.com/KittingKitten')
html = response.read()
soup = BeautifulSoup(html)
