from _sendrequest_ import send_request


def arrayconnections(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

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

    ENDPOINT =  f'api/{API_VERSION}/array-connections'
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }
    VALIDATE_METHODS = ['GET', 'PATCH', 'POST', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, arrayconnections_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def arrayconnections_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'remote_ids' in PARAMS and 'remote_names' in PARAMS:
            print("Error: 'remote_ids' and 'remote_names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'filter', 'ids', 'limit', 'offset', 'remote_ids', 'remote_names', 'sort'}
    elif METHOD in ['PATCH', 'DELETE']:
        if 'remote_ids' in PARAMS and 'remote_names' in PARAMS:
            print("Error: 'remote_ids' and 'remote_names' cannot be provided at the same time.")
            return False
        valid_fields = {'ids', 'remote_ids', 'remote_names'}
    elif METHOD in ['POST']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'encrypted', 'management_address', 'replication_addresses', 'connection_key', 'throttle'}
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True


def arrayconnections_connectionkey(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):
    
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
    ENDPOINT =  f'api/{API_VERSION}/array-connections/connection-key'
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }
    VALIDATE_METHODS = ['GET', 'POST']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, arrayconnections_connectionkey_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def arrayconnections_connectionkey_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'filter', 'ids', 'limit', 'names', 'offset', 'sort'}
    elif METHOD in ['POST']:
        valid_fields = {}
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True



def arrayconnections_path(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    ENDPOINT =  f'api/{API_VERSION}/array-connections/path'
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }
    VALIDATE_METHODS = ['GET']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, arrayconnections_path_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def arrayconnections_path_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'remote_ids' in PARAMS and 'remote_names' in PARAMS:
            print("Error: 'remote_ids' and 'remote_names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'filter', 'ids', 'limit', 'offset', 'remote_ids', 'remote_names', 'sort'}
   
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True



def arrayconnections_performance_replication(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT =  f'api/{API_VERSION}/array-connections/performance/replication'
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }
    VALIDATE_METHODS = ['GET']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, arrayconnections_performance_replication_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def arrayconnections_performance_replication_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'remote_ids' in PARAMS and 'remote_names' in PARAMS:
            print("Error: 'remote_ids' and 'remote_names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'end_time', 'filter', 'ids', 'limit', 'offset', 'remote_ids', 'remote_names', 'resolution', 'sort', 'start_time', 'total_only', 'type'}
   
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True
