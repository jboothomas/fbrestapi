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

    ENDPOINT = f'api/{API_VERSION}/buckets'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, buckets_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def buckets_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'destroyed', 'filter', 'ids', 'limit', 'names', 'offset', 'sort', 'total_only'}
    elif METHOD in ['POST']:
        if not 'names' in PARAMS:
            print("Error 'names' is required.")
            return False
        valid_fields = {'names'}
    elif METHOD in ['PATCH']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'ids', 'ignore_usage', 'names'}
    elif METHOD in ['DELETE']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'ids', 'names'}
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True 



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