import requests


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

