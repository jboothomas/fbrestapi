from _sendrequest_ import send_request


def arrays(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ## Example application/json payload
    #{
    #  "name": "string",
    #  "banner": "Restricted area. Authorized personnel only.",
    #  "idle_timeout": 300000,
    #  "ntp_servers": [
    #    "time.acme.com"
    #  ],
    #  "time_zone": "America/Los_Angeles"
    #}

    ENDPOINT = f'api/{API_VERSION}/arrays'
    VALIDATE_METHODS = ['GET', 'PATCH']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, arrays_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def arrays_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        valid_fields = {'continuation_token', 'filter', 'limit', 'offset', 'sort'}
    if METHOD in ['PATCH']:
        valid_fields = {}
  
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True 


def arrays_eula(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    ## Example application/json payload
    #{
    #  "signature": {
    #    "name": "Nice Guy",
    #    "title": "Admin",
    #    "company": "Pure Storage Inc."
    #  }
    #}
   
    ENDPOINT = f'api/{API_VERSION}/arrays/eula'
    VALIDATE_METHODS = ['GET', 'PATCH']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, arrays_eula_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def arrays_eula_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        valid_fields = {'continuation_token', 'filter', 'limit', 'offset', 'sort'}
    if METHOD in ['PATCH']:
        valid_fields = {}
  
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True   


def arrays_factoryresettoken(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/arrays/factory-reset-token'
    VALIDATE_METHODS = ['GET', 'DELETE', 'POST']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, arrays_factoryresettoken_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def arrays_factoryresettoken_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        valid_fields = {'continuation_token', 'filter', 'limit', 'offset', 'sort'}
    if METHOD in ['DELETE', 'POST']:
        valid_fields = {}
  
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True    


def arrays_httpspecificperformance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/arrays/http-specific-performance'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, arrays_httpspecificperformance_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def arrays_httpspecificperformance_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        valid_fields = {'end_time', 'resolution', 'start_time'}
  
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True

    
def arrays_nfsspecificperformance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/arrays/nfs-specific-performance'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, arrays_nfsspecificperformance_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def arrays_nfsspecificperformance_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        valid_fields = {'end_time', 'resolution', 'start_time'}
  
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True


def arrays_performance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/arrays/performance'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, arrays_performance_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def arrays_performance_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        valid_fields = {'end_time', 'protocol', 'resolution', 'start_time'}
  
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True


def arrays_performance_replication(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/arrays/performance/replication'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, arrays_performance_replication_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def arrays_performance_replication_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        valid_fields = {'end_time', 'resolution', 'start_time', 'type'}
  
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True


def arrays_s3specificperformance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/arrays/s3-specific-performance'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, arrays_s3specificperformance_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def arrays_s3specificperformance_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        valid_fields = {'end_time', 'resolution', 'start_time'}
  
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True


def arrays_space(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/arrays/space'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, arrays_space_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def arrays_space_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        valid_fields = {'end_time', 'resolution', 'start_time', 'type'}
  
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True
    

def arrays_supportedtimezones(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/arrays/supported-time-zones'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, arrays_supportedtimezones_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def arrays_supportedtimezones_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        valid_fields = {'continuation_token', 'filter', 'limit', 'names', 'offset', 'sort'}
  
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True

    

def arrays_clients_performance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/arrays/clients/performance'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, arrays_clients_performance_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def arrays_clients_performance_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:

        valid_fields = {'filter', 'limit', 'names', 'sort', 'total_only'}
    
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True