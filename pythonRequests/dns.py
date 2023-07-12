import requests
import json
from _sendrequest_ import send_request



def dns(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ## Example application/json payload
    #{
    #  "domain": "example.com",
    #  "nameservers": [
    #    "192.168.0.125"
    #  ]
    #}

    ENDPOINT = f'api/{API_VERSION}/dns'
    VALIDATE_METHODS = ['GET', 'PATCH']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, dns_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def dns_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'filter', 'ids', 'limit', 'names', 'offset', 'sort'}
    elif METHOD in ['PATCH']:
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