import requests
import json

def get_arrays(FB_IP, X_AUTH_TOKEN, API_VERSION):
    url = f"https://{FB_IP}/api/{API_VERSION}/arrays"
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }

    response = requests.get(
        url,
        headers=headers,
        verify=False  # consider removing this if your FB has a valid SSL cert
    )

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Request to {url} failed with status code {response.status_code}')
        return None

def patch_arrays(FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):
    url = f"https://{FB_IP}/api/{API_VERSION}/arrays"
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }
    # Convert payload to JSON
    payload = json.dumps(PAYLOAD)

    response = requests.patch(
        url, 
        headers=headers, 
        data=payload,
        verify=False  # consider removing this if your FB has a valid SSL cert
    )

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Request to {url} failed with status code {response.status_code}')
        return None