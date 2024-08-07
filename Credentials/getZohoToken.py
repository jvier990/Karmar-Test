import requests
from dotenv import load_dotenv
import os
load_dotenv()


def get_access_token(refresh_token, client_id, client_secret):
    url = "https://accounts.zoho.com/oauth/v2/token"
    params = {
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'refresh_token'
    }
    
    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
        data = response.json()
        access_token = data.get('access_token')
        return access_token
    
    except requests.RequestException as e:
        print(f"Error al obtener el access_token: {e}")
        return None

if __name__ == "__main__":

    refresh_token = os.getenv('REFRESH_TOKEN')
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    print(client_id)
    
    access_token = get_access_token(refresh_token, client_id, client_secret)
    
    if access_token:
        print(f"Access Token: {access_token}")
    else:
        print("No se pudo obtener el Access Token.")
