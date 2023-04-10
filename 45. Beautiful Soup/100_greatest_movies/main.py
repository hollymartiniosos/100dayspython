import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

req = requests.get(URL)
soup = BeautifulSoup(req.content, "html.parser")
script = soup.find("script", type="application/json")
data = json.loads(script.string)
# with open("website.json", "w") as file:
#     json.dump(data, file)
# print(data)
movies = []
for film in data["props"]["pageProps"]["data"]["getArticleByFurl"]["_layout"][3]["content"]["images"]:
    # print(film["titleText"])
    movies.append(film["titleText"])
new_movies = movies[::-1]
print(new_movies)  

with open("movies.txt", "w", encoding="utf8") as output:
    output.write("\n".join(new_movies))



# indexs_list = []
# titles_list= []
# for i in movies:
#     new_list = i.split(")")
#     index = new_list[0]
#     indexs_list.append(index)
#     title = new_list[2]
#     titles_list.append(title)

# print(indexs_list)
# print(titles_list)    

# response = requests.get(URL)
# website_html = response.text
# # print(website_html)
# soup = BeautifulSoup(website_html, "html.parser")


# # title = soup.find(name="div", class_="jsx-1456218620 article-content")

# divs= soup.find_all(name="div", class_ = "jsx-3523802742 listicle-item")
# print(len(divs))
# for div in divs:

# # title = str(div).find("h3")
# # print(title)