from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# Pull the title of the first article
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.find(name="a").get("href"))

# Split to only get number for score instead of 'number points'
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

# Print the article and link with the most upvotes
max_index = article_upvotes.index(max(article_upvotes))
print(article_texts[max_index])
print(article_links[max_index])

















# # Add encoding to avoid UnicodeDecodeError: 'cp950' codec can't decode byte 0xe2 in position 280: illegal multibyte sequence
# # Error is due to the heart emoji
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# #print(soup.title)
# #print(soup.title.string)

# # Indents the tags
# #print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     #print(tag.getText())
#     #print(tag.get("href"))
#     pass

# heading = soup.find(name="h1", id="name")
# #print(heading)

# # class_ to avoid clashing with class which is a keyword that creates a class
# section_heading = soup.find(name="h3", class_="heading")

# # Selects the first a in p. Can use selector="#name" for id
# company_url = soup.select_one(selector="p a")

# # Select all with class of "heading"
# headings = soup.select(".heading")