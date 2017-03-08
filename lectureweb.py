import bs4, urllib, base64

URL="https://twitter.com/morpheeDgami"

page = urllib.urlopen(URL)
data=page.read().decode('UTF-8')
soup=bs4.BeautifulSoup(data, 'html.parser')

recup=soup.findAll(attrs={"class":"js-tweet-text-container"})

tweet=[]
for i in recup:
    tweet.append(i.getText())

# Affichage classique
# print tweet[0]

# Affichage avec une converssion du base64
print base64.b64decode(tweet[0])
