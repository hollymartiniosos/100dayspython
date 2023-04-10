from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")
# finding details for first article
# article_tag = soup.find(name="span", class_="titleline").select_one(selector="a")
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()
# print(article_text)
# print(article_link)
# print(article_upvote)

# finding details for all articles
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.select_one(selector="a").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_score = article_upvotes.index(max(article_upvotes))

print(article_texts[max_score])
print(article_links[max_score])
print(article_upvotes[max_score])

    
    
