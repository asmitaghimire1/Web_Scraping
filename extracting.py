from bs4 import BeautifulSoup
import pandas as pd

with open("imdb.html", "r", encoding = 'utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

titles = []
ratings = []
year = []

for tag in soup.find_all("a", class_="ipc-title-link-wrapper"):
    title = tag.h3.text.split(". ", 1)[1]
    titles.append(title)

for rating in soup.find_all("span", class_="ipc-rating-star--rating"):
    ratings.append(rating.text)

for y in soup.find_all("div", class_="sc-15ac7568-6 fqJJPW cli-title-metadata"):
    spans = y.find_all("span")      # get all spans inside the div
    if len(spans) >= 1:             # make sure there is at least one span
        ye = spans[0].text.strip()  # first span → year
        year.append(ye)


df = pd.DataFrame({
    "Title": titles,
    "Year": year,
    "Rating": ratings,
})

df.to_csv("imdb_top_movies.csv", index = False)
