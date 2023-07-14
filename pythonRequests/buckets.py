from _sendrequest_ import send_request


def buckets(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

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



def buckets_performance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/buckets/performance'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, buckets_performance_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def buckets_performance_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'end_time', 'filter', 'ids', 'limit', 'names', 'offset', 'resolution', 'sort', 'start_time', 'total_only'}

    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True 

def buckets_s3specificperformance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/buckets/s3-specific-performance'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, buckets_s3specificperformance_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def buckets_s3specificperformance_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'end_time', 'filter', 'ids', 'limit', 'names', 'offset', 'resolution', 'sort', 'start_time', 'total_only'}

    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True 