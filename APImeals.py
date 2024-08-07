import requests


class ApiMeal:
    def __init__(self, base_url):
        self.base_url = base_url


    def get_meals(self, by,value):
        url = f"{self.base_url}{by}{value}"
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: No se pudo obtener datos de la API")
            return None

    def get_categories(self):
        url = f"https://www.themealdb.com/api/json/v1/1/categories.php"
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: No se pudo obtener datos de la API")
            return None
