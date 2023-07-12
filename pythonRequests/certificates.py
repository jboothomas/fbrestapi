import requests
import json


def certificates(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    ## Example application/json payload
    #{
    #  "certificate": "string",
    #  "intermediate_certificate": "string",
    #  "passphrase": "string",
    #  "private_key": "string"
    #}

    url = f"https://{FB_IP}/api/{API_VERSION}/certificates"
    
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

def certificates_certificategroups(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    url = f"https://{FB_IP}/api/{API_VERSION}/certificates/certificte-groups"
    
    if METHOD not in ['GET', 'POST', 'DELETE']:
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

def certificates_uses(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    url = f"https://{FB_IP}/api/{API_VERSION}/certificates/uses"
    
    if METHOD not in ['GET']:
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