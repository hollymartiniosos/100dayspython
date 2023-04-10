from bs4 import BeautifulSoup

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(  contents, "html.parser")    
print(soup.title)
print(soup.prettify())

all_anchor_tags = soup.find_all(name="a")

for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)    

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

company_url2 = soup.select_one(selector="#name")
print(company_url2)

company_url3 = soup.select_one(selector=".heading")
print(company_url)

headings = soup.select(".heading")
print(headings)