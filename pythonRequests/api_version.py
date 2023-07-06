import requests
import json

FB_IP = '<YOUR_FLASHBLADE_IP>'


# Get API versions
url = f"https://{FB_IP}/api/api_version"

version_response = requests.get(
    url,
    verify=False  # consider removing this if your FB has a valid SSL cert
)

if version_response.status_code == 200:
    data = version_response.json()
    versions = data['versions']
else:
    print(f'Request failed with status code {version_response.status_code}')
    exit(1)

print(versions)
