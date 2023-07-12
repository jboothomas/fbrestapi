from _sendrequest_ import send_request



def certificategroups(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/certificate-groups'
    VALIDATE_METHODS = ['GET', 'POST', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, certificategroups_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def certificategroups_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'filter', 'ids', 'limit', 'names', 'offset', 'sort'}
    elif METHOD in ['POST']:
        valid_fields = {'names'}
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



def certificategroups_certificates(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/certificate-groups/certifictes'
    VALIDATE_METHODS = ['GET', 'POST', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, certificategroups_certificates_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def certificategroups_certificates_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'certificate_ids' in PARAMS and 'certificate_names' in PARAMS:
            print("Error: 'certificate_ids' and 'certificate_names' cannot be provided at the same time.")
            return False
        if 'certificate_group_ids' in PARAMS and 'certificate_group_names' in PARAMS:
            print("Error: 'certificate_group_ids' and 'certificate_group_names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'certificate_ids', 'certificate_group_ids', 'certificate_group_names', 'certificate_names', 'filter', 'limit', 'offset', 'sort'}
    elif METHOD in ['POST', 'DELETE']:
        if 'certificate_ids' in PARAMS and 'certificate_names' in PARAMS:
            print("Error: 'certificate_ids' and 'certificate_names' cannot be provided at the same time.")
            return False
        if 'certificate_group_ids' in PARAMS and 'certificate_group_names' in PARAMS:
            print("Error: 'certificate_group_ids' and 'certificate_group_names' cannot be provided at the same time.")
            return False
        valid_fields = {'certificate_ids', 'certificate_group_ids', 'certificate_group_names', 'certificate_names',}
 
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True


def certificategroups_uses(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/certificate-groups/uses'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, certificategroups_uses_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def certificategroups_uses_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'filter', 'ids', 'limit', 'names', 'offset', 'sort'}

    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True