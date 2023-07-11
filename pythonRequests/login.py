import requests

def login(FB_IP, API_TOKEN):

    # Authenticate and get X-Auth-Token
    url = f"https://{FB_IP}/api/login"
    headers = {
      'api-token': API_TOKEN
    }

    login_response = requests.post(
        url,
        headers=headers,
        verify=False  # consider removing this if your FB has a valid SSL cert
    )

    if login_response.status_code == 200:
        X_AUTH_TOKEN = login_response.headers.get('X-Auth-Token')
        return X_AUTH_TOKEN
    else:
        print(f'Authentication failed with status code {login_response.status_code}')
        return None

