import requests
import json


def buckets(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    ##Example application/json payload
    #{
    #  "destroyed": true,
    #  "hard_limit_enabled": true,
    #  "object_lock_config": {
    #    "default_retention_mode": "governance",
    #    "enabled": true,
    #    "freeze_locked_objects": true,
    #    "default_retention": "86400000"
    #  },
    #  "quota_limit": "string",
    #  "retention_lock": "unlocked",
    #  "versioning": "string"
    #}

    url = f"https://{FB_IP}/api/{API_VERSION}/buckets"
    
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
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'{METHOD} request to {url} failed with status code {response.status_code} error message: {errormessage}')
        return None

def buckets_performance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    url = f"https://{FB_IP}/api/{API_VERSION}/buckets/performance"
    
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
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'{METHOD} request to {url} failed with status code {response.status_code} error message: {errormessage}')
        return None

def buckets_s3specificperformance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    url = f"https://{FB_IP}/api/{API_VERSION}/buckets/s3-specific-performance"
    
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
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'{METHOD} request to {url} failed with status code {response.status_code} error message: {errormessage}')
        return None