import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Get and save raw html text
response = requests.get(URL)
response.raise_for_status()
text = response.text

soup = BeautifulSoup(text, "html.parser")

# Find all the titles of movies and add to list
titles = soup.find_all(name="h3", class_="title")
titles_list = [title.getText() for title in titles]

# Save the titles in reverse order in a txt
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in reversed(titles_list):
        file.write(f"{movie}\n")
