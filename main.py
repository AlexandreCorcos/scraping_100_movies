import requests
from bs4 import BeautifulSoup
import html

file_path = "movies.txt"

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

URL_ONLINE = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
eo_web_page = response.text

soup = BeautifulSoup(eo_web_page, "html.parser")

all_titles = soup.findAll(name="h3", class_="title")

title_list = [title.getText() for title in all_titles]

inverse_list = title_list[::-1]

with open(file_path, "w", encoding='utf-8') as file:
    for unescape_item in inverse_list:
        item = html.unescape(unescape_item)
        file.write(item + "\n")

