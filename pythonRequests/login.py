import requests

FB_IP = '<YOUR_FLASHBLADE_IP>'
API_TOKEN = '<YOUR_FB_API_TOKEN>'


# Authenticate and get X-Auth-Token
url = f"https://{FB_IP}/api/login"
headers = {
  'api-token': API_TOKEN
}

auth_response = requests.post(
    url,
    headers=headers,
    verify=False  # consider removing this if your FB has a valid SSL cert
)

if auth_response.status_code == 200:
    token = auth_response.headers.get('X-Auth-Token')
else:
    print(f'Authentication failed with status code {auth_response.status_code}')
    exit(1)

print(token)

