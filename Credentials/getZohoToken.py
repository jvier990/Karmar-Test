import requests

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

