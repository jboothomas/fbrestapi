import requests
import json


def bucketreplicalinks(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    url = f"https://{FB_IP}/api/{API_VERSION}/bucket-replica-links"
    
    if METHOD not in ['GET', 'POST', 'PATCH', 'DELETE']:
        print(f'The method "{METHOD}" is not valid for {url}.')
        return
    
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }
    # Convert payload to JSON
    payload = json.dumps(PAYLOAD)

    response = requests.request(
        METHOD,
        url, 
        headers=headers, 
        data=payload,
        verify=False  # consider removing this if your FB has a valid SSL cert
    )

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'{METHOD} request to {url} failed with status code {response.status_code}')
        return None