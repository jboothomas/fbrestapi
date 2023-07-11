import requests

def get_arrays(FB_IP, X_AUTH_TOKEN, API_VERSION):
    url = f"https://{FB_IP}/api/{API_VERSION}/arrays"
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }

    arrays_response = requests.get(
        url,
        headers=headers,
        verify=False  # consider removing this if your FB has a valid SSL cert
    )

    if arrays_response.status_code == 200:
        data = arrays_response.json()
        return data
    else:
        print(f'Request to {url} failed with status code {arrays_response.status_code}')
        return None