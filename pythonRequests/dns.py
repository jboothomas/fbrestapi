import requests
import json


def dns(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    ## Example application/json payload
    #{
    #  "domain": "example.com",
    #  "nameservers": [
    #    "192.168.0.125"
    #  ]
    #}

    url = f"https://{FB_IP}/api/{API_VERSION}/dns"
    
    if METHOD not in ['GET', 'PATCH']:
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
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'{METHOD} request to {url} failed with status code {response.status_code} error message: {errormessage}')
        return None