from bs4 import BeautifulSoup
import requests

#PART 2 - Use real website
response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article_title = [content.find('a').text.strip() for content in soup.select('span.titleline')]
article_link = [content.find('a').get("href") for content in soup.select('span.titleline')]
article_score = [score.getText().split()[0] for score in soup.select('span.score')]

# print(article_title)
# print(article_link)
# print(article_score)

index_of_highest = article_score.index(max(article_score))
print(index_of_highest)
print(article_title[index_of_highest])
print(article_score[index_of_highest])

#PART 1
# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

#1) print HTML in pretty way
#print(soup.prettify())

#2) look for all anchor tags elements
# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.getText())

#3) find one element with unique id name
# heading = soup.find(name="h1", id="name")
# print(heading.getText())

#4) find a class
# section_heading = soup.find(name="h3", class_ = "heading")
# print(section_heading)

#5) select first matching item
# company_url = soup.select_one(selector="p a")
# print(company_url.getText())

#6) select all matching items (list)
# headings = soup.select(".heading")
# print(headings)