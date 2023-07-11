import requests

def login(FB_IP, API_TOKEN):

    # Authenticate and get X-Auth-Token
    url = f"https://{FB_IP}/api/login"
    headers = {
      'api-token': API_TOKEN
    }

    response = requests.post(
        url,
        headers=headers,
        verify=False  # consider removing this if your FB has a valid SSL cert
    )

    if response.status_code == 200:
        X_AUTH_TOKEN = response.headers.get('X-Auth-Token')
        return X_AUTH_TOKEN
    else:
        print(f'Authentication failed with status code {response.status_code}')
        return None

