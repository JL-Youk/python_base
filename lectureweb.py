import bs4, urllib

URL="https://twitter.com/morpheeDgami"

page = urllib.urlopen(URL)
data=page.read().decode('UTF-8')
soup=bs4.BeautifulSoup(data, 'html.parser')

recup=soup.findAll(attrs={"class":"js-tweet-text-container"})

tweet=[]
for i in recup:

print (base64.b64decode(tweet[0]))
