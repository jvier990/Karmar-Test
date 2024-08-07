import requests
import json

class ApiMeal:
    def __init__(self, base_url):
        self.base_url = base_url


    def get_meals_by_category(self, category):
        url = f"{self.base_url}{category}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: No se pudo obtener datos de la API")
            return None

    def get_meal_details(self,meal_id):
        url = f"{self.base_url}{meal_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: No se pudo obtener detalles del plato")
            return None
    
