import json

def mealsMapper(mealsCategories):
    data = mealsCategories
    id_meals = [meal['idMeal'] for meal in data['meals']]
    return id_meals
