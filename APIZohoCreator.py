import requests
import json


class ApiZoho:
    def __init__(self, base_url, auth_token, environment):
        self.base_url = base_url
        self.auth_token = auth_token
        self.environment = environment

    def get_general_data(self):
        url = f"{self.base_url}/All_Meals"
        headers = {
            'Authorization': f'Zoho-oauthtoken {self.auth_token}',
            'environment': self.environment
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  
            return response.json()  
        except requests.RequestException as e:
            print(f"Error al hacer la solicitud GET: {e}")
            return None
        
    def get_general_categories_data(self):
        url = f"{self.base_url}/All_Categories"
        headers = {
            'Authorization': f'Zoho-oauthtoken {self.auth_token}',
            'environment': self.environment
        }

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  
            return response.json()  
        except requests.RequestException as e:
            print(f"Error al hacer la solicitud GET: {e}")
            return None
        
    def add_meals(self, meal_data):
        url = f"{self.base_url}/Meals"
        headers = {
            'Authorization': f'Zoho-oauthtoken {self.auth_token}',
            'environment': self.environment,
            'Content-Type': 'application/json'  # Asegúrate de especificar que el contenido es JSON
        }

        # Convierte el dict a JSON si no está ya en formato JSON
        if isinstance(meal_data, dict):
            meal_data = json.dumps(meal_data)

        try:
            # Realiza la solicitud POST
            response = requests.post(url, headers=headers, data=meal_data)
            response.raise_for_status()  # Verifica si hubo un error en la respuesta

            # Devuelve la respuesta JSON si fue exitosa
            print('EXITOOOO')
            return response.json()
        except requests.RequestException as e:
            print(f"Error al hacer la solicitud POST: {e}")
            return None

    def add_categories(self, categorie_data):
        url = f"{self.base_url}/Categories"
        headers = {
            'Authorization': f'Zoho-oauthtoken {self.auth_token}',
            'environment': self.environment,
            'Content-Type': 'application/json'  # Asegúrate de especificar que el contenido es JSON
        }


        # Convierte el dict a JSON si no está ya en formato JSON
        if isinstance(categorie_data, dict):
            categorie_data = json.dumps(categorie_data)

        try:
            # Realiza la solicitud POST
            response = requests.post(url, headers=headers, data=categorie_data)
            response.raise_for_status()  # Verifica si hubo un error en la respuesta

            # Devuelve la respuesta JSON si fue exitosa
            print('EXITOOOO')
            return response.json()
        except requests.RequestException as e:
            print(f"Error al hacer la solicitud POST: {e}")
            return None

       


