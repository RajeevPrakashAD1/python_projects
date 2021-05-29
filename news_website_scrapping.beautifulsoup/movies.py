import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movie_web = response.text
soup = BeautifulSoup(movie_web,"html.parser")

name_of_movies  = soup.findAll(name="h3",class_="title")
print(name_of_movies)

movie_file =  open("movies.txt", "r+")

for i in range(len(name_of_movies)-1,0,-1):
    if i==100-58 or  i == 100-59:
        pass
    else:

        movie_file.write(name_of_movies[i].getText())
        movie_file.write("\n")
movie_file.close()