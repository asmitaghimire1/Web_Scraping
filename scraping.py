import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

r = requests.get(url, headers=headers)

with open("imdb.html", "w", encoding="utf-8") as f:
    f.write(r.text)

with open("imdb.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# To make the html code pretty 
print(soup.prettify())

# To access title tag 
print("Title tag: ", soup.title)

# Get the name of the title tag
print("Title tag name: ",soup.title.name)

# Get the string within the title tag
print("Title tag string: ",soup.title.string)

# Get the parent name of the title 
print("Title tag parent name: ",soup.title.parent.name)

#Access the first paragraph tag
print("First paragraph tag: ",soup.p )

#Class attribute of the first paragraph tag
print("Class attribute of the First paragraph: ",soup.p['class'] )

#Access the first anchor tag
print("First Anchor tag: ",soup.a)

# Access all anchor tag
print("Anchor tags: ",soup.find_all('a'))

# Access the tag with id
print("Tag with id - home_img: ", soup.find(id = 'home_img'))