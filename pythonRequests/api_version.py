import requests
import json

def api_version(FB_IP):
    # Get API versions
    url = f"https://{FB_IP}/api/api_version"

    version_response = requests.get(
       url,
        verify=False  # consider removing this if your FB has a valid SSL cert
    )

    if version_response.status_code == 200:
        data = version_response.json()
        API_VERSIONS = data['versions']
        return API_VERSIONS
    else:
        print(f'Request to {url} failed with status code {version_response.status_code}')
        return None

