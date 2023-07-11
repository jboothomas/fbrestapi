import requests
import json


def array_connections(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    ## Example application/json payload
    #{{
    #  "encrypted": true,
    #  "management_address": "10.202.101.78",
    #  "replication_addresses": [
    #    "10.202.101.70"
    #  ],
    #  "throttle": {
    #    "default_limit": 1073741824,
    #    "window": {
    #      "start": 3600000,
    #      "end": 46800000
    #    },
    #    "window_limit": 2097152
    #  }
    #}

    url = f"https://{FB_IP}/api/{API_VERSION}/array-connections"
    
    if METHOD not in ['GET', 'PATCH', 'POST', 'DELETE']:
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

def array_connections_connectionkey(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):
    
    ## Example application/json payload
    #{
    #  "items": [
    #    {
    #      "connection_key": "6207d123-d123-0b5c-5fa1-95fabc5c7123",
    #      "created": 0,
    #      "expires": 0
    #    }
    #  ]
    #}

    url = f"https://{FB_IP}/api/{API_VERSION}/array-connections/connection-key"

    if METHOD not in ['GET', 'POST']:
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

def array_connections_path(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):
    url = f"https://{FB_IP}/api/{API_VERSION}/array-connections/path"

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

def array_connections_performance_replication(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):
    url = f"https://{FB_IP}/api/{API_VERSION}/array-connections/performance/replication"

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