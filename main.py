
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import defaultdict

os.environ['PATH'] += r"C:/ChromeWebDrivers"
driver  = webdriver.Chrome()
driver.get("https://www.imdb.com/chart/top/")
movies = driver.find_elements(By.CLASS_NAME,"ipc-title-link-wrapper")

movies_list = [ movie.text for movie in movies]

del movies_list[-8:]

def clean_title(title):
    return ' '.join(title.split()[1:])

cleaned_movies_list = [clean_title(movie) for movie in movies_list]
cleaned_movies_list.sort()

title_number = []

for title in cleaned_movies_list:
   if title[0].isdigit():
        title_number.append(title)

movies_list_by_letter = defaultdict(list)

for movie in cleaned_movies_list:
    first_letter = movie[0].upper()
    movies_list_by_letter[first_letter].append(movie)

for letter,movies in movies_list_by_letter.items():
    print(f"{letter} {movies}")















