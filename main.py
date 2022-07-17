# Input a recipe URL from allrecipes.com and receive the ingredient list and directions.

import requests
from bs4 import BeautifulSoup


# Gets the webpage and parses with BeautifulSoup. Returns a list of ingredients.
def get_ingredients(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(class_='recipe-content-container')
    ingredient_section = results.find('ul', class_='ingredients-section')

    ingredients = [ingredient.text.strip() for ingredient in ingredient_section if ingredient.text.strip()]

    return ingredients


# Gets the webpage and parses with BeautifulSoup. Returns a list of directions.
def get_directions(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(class_='recipe-content-container')
    instructions_section = results.find('ul', class_='instructions-section')

    directions = [step.text.strip() for step in instructions_section if step.text.strip()]

    # Removes the word "Advertisement" from the list of directions, if present.
    for x in range(len(directions)):
        if directions[x][-13:] == 'Advertisement':
            directions[x] = directions[x][:-13].strip()


    return directions


# Sample URL = 'https://www.allrecipes.com/recipe/275553/breaded-air-fryer-pork-chops/'
URL = input()

ingredient_list = get_ingredients(URL)
direction_list = get_directions(URL)

print('Ingredients')
for ingredient in ingredient_list:
    print(ingredient)

print('\n')

print('Directions')
for direction in direction_list:
    print(direction)
