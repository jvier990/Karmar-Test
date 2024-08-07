import os
from APIZohoCreator import ApiZoho
from APImeals import ApiMeal
from Credentials.getZohoToken import get_access_token
from dotenv import load_dotenv
load_dotenv()

refresh_token = os.getenv('REFRESH_TOKEN')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
username = os.getenv('USERNAME_ZOHO')
app = os.getenv('APP')
report_url = os.getenv('REPORT_URL')
environment = os.getenv('ENVIRONMENT')

meal_url = os.getenv('MEAL_BASE_URL')

auth_token = get_access_token(refresh_token, client_id, client_secret)



report_url = f"{report_url}/{username}/{app}/report"
backend = ApiZoho(report_url, auth_token, environment)
meals = ApiMeal(meal_url)
    

data = backend.get_general_data()
    
if data:
    print("Datos obtenidos:", data)
else:
    print("No se pudo obtener datos.")


meals_data = meals.get_meals_by_category('Seafood')
    
if meals_data:
    print("Datos obtenidos:", meals_data)
else:
    print("No se pudo obtener datos.")