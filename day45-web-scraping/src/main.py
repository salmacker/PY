from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

h2_tags = soup.find_all('h2')

film_list = [h2.find('strong').getText() if h2.find('strong') else None for h2 in h2_tags]
result = film_list.reverse()
film_list = film_list[:100]

with open('top100-movies.txt', 'w',encoding='utf-8') as file:
    for film in film_list:
        file.write(f'{film}\n')
