from _sendrequest_ import send_request


def bucketreplicalinks(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ## Example application/json payload
    #{
    #  "paused": true,
    #  "remote_credentials": {
    #    "id": "string",
    #    "name": "string"
    #  }
    #}

    ENDPOINT = f'api/{API_VERSION}/bucket-replica-links'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, bucketreplicalinks_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def bucketreplicalinks_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        if 'local_bucket_ids' in PARAMS and 'local_bucket_names' in PARAMS:
            print("Error: 'local_bucket_ids' and 'local_bucket_names' cannot be provided at the same time.")
            return False
        if 'remote_ids' in PARAMS and 'remote_names' in PARAMS:
            print("Error: 'remote_ids' and 'remote_names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'filter', 'ids', 'local_bucket_ids', 'local_bucket_names', 'remote_ids', 'remote_names', 'sort', 'total_only'}
    elif METHOD in ['POST']:
        if 'local_bucket_ids' in PARAMS and 'local_bucket_names' in PARAMS:
            print("Error: 'local_bucket_ids' and 'local_bucket_names' cannot be provided at the same time.")
            return False
        if 'remote_credentials_ids' in PARAMS and 'remote_credentials_names' in PARAMS:
            print("Error: 'remote_credentials_ids' and 'remote_credentials_names' cannot be provided at the same time.")
            return False
        valid_fields = {'local_bucket_ids', 'local_bucket_names', 'remote_bucket_names', 'remote_credentials_names', 'remote_credentials_ids'}
    elif METHOD in ['PATCH', 'DELETE']:
        if 'local_bucket_ids' in PARAMS and 'local_bucket_names' in PARAMS:
            print("Error: 'local_bucket_ids' and 'local_bucket_names' cannot be provided at the same time.")
            return False
        if 'remote_ids' in PARAMS and 'remote_names' in PARAMS:
            print("Error: 'remote_ids' and 'remote_names' cannot be provided at the same time.")
            return False
        valid_fields = {'ids', 'local_bucket_ids', 'local_bucket_names', 'remote_bucket_names', 'remote_ids', 'remote_names'}
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True 