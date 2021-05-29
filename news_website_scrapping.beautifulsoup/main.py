import requests
from bs4 import BeautifulSoup
response = requests.get("https://news.ycombinator.com/")

y_combinator_webpage = response.text
soup = BeautifulSoup(y_combinator_webpage,"html.parser")



text = []
link = []
anchor_tags = soup.findAll(name="a",class_="storylink")


for tag in anchor_tags:
    link.append(tag.get("href"))
    text.append(tag.getText())

votes = []
voting = soup.findAll(name="span", class_="score")
for i in voting:

    votes.append(int(i.getText().split()[0]))

# print(votes)
# print(link)
max_votes = max(votes)
index_maxvotes =  votes.index(max_votes)
print(max_votes,link[index_maxvotes],text[index_maxvotes])