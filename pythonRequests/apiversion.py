import requests
import json

def apiversion(FB_IP):
    # Get API versions
    url = f"https://{FB_IP}/api/api_version"

    response = requests.request(
        'GET',
        url,
        verify=False  # consider removing this if your FB has a valid SSL cert
    )

    if response.status_code == 200:
        data = response.json()
        API_VERSIONS = data['versions']
        return API_VERSIONS
    else:
        print(f'Request to {url} failed with status code {response.status_code}')
        return None
