from _sendrequest_ import send_request


def filesystemsnapshots(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ## Example application/json payload
    #{
    #  "suffix": "string"
    #}

    ENDPOINT = f'api/{API_VERSION}/file-system-snapshots'
    VALIDATE_METHODS = ['GET', 'POST', 'DELETE', 'PATCH']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystemsnapshots_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystemsnapshots_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'ids' in PARAMS and 'owner_ids' in PARAMS:
            print("Error: 'ids' and 'owner_ids' cannot be provided at the same time.")
            return False
        if 'owner_ids' and 'names_or_owner_names' in PARAMS:
            print("Error: 'owner_ids' and 'names_or_owner_names' cannot be provided at the same time.")
        valid_fields = {'continuation_token', 'destroyed', 'filter', 'ids', 'limit', 'names_or_owner', 'offset', 'owner_ids', 'sort', 'total_only'}

    elif METHOD in ['POST']:
        if 'source_ids' in PARAMS and 'source_names' in PARAMS:
            print("Error: 'source_ids' and 'source_names' cannot be provided at the same time.")
            return False
        valid_fields = {'source_ids', 'source_names', 'send', 'targets'}

    elif METHOD in ['DELETE']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'ids', 'names'}
    
    elif METHOD in ['PATCH']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = { 'ids', 'latest_replica', 'names'}

    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True


def filesystemsnapshots_policies(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-system-snapshots/policies'
    VALIDATE_METHODS = ['GET', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }
    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystemsnapshots_policies_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystemsnapshots_policies_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'member_ids' in PARAMS and 'member_names' in PARAMS:
            print("Error: 'member_ids' and 'member_names' cannot be provided at the same time.")
            return False
        if 'policy_ids' in PARAMS and 'policy_names' in PARAMS:
            print("Error: 'policy_ids' and 'policy_names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'filter', 'limit', 'member_ids', 'member_names', 'offset', 'policy_ids', 'policy_names', 'sort'}
    
    if METHOD in ['DELETE']:
        if 'member_ids' in PARAMS and 'member_names' in PARAMS:
            print("Error: 'member_ids' and 'member_names' cannot be provided at the same time.")
            return False
        if 'policy_ids' in PARAMS and 'policy_names' in PARAMS:
            print("Error: 'policy_ids' and 'policy_names' cannot be provided at the same time.")
            return False
        valid_fields = {'member_ids', 'member_names', 'policy_ids', 'policy_names'}
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True

def filesystemsnapshots_transfer(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-systemsnapshots/transfer'
    VALIDATE_METHODS = ['GET', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }    
    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystemsnapshots_transfere_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystemsnapshots_transfere_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        valid_fields = {'continuation_token', 'filter', 'ids', 'limit', 'names_or_owner_names', 'offset', 'sort', 'total_only'}
    
    if METHOD in ['DELETE']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        if 'remote_ids' in PARAMS and 'remote_names' in PARAMS:
            print("Error: 'remote_ids' and 'remote_names' cannot be provided at the same time.")
            return False         
        valid_fields = {'ids', 'names', 'remote_names', 'remote_ids'}
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True
    

def filesystems_policies(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-systems/policies'
    VALIDATE_METHODS = ['GET', 'POST', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }
    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_policies_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystems_policies_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'member_ids' in PARAMS and 'member_names' in PARAMS:
            print("Error: 'member_ids' and 'member_names' cannot be provided at the same time.")
            return False
        if  'policy_ids' in PARAMS and 'policy_names' in PARAMS:
            print("Error: 'policy_ids' and 'policy_names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'filter', 'limit', 'member_ids', 'member_names', 'offset', 'policy_ids', 'policy_names', 'sort'}
    
    elif METHOD in ['POST', 'DELETE']:
        if 'member_ids' in PARAMS and 'member_names' in PARAMS:
            print("Error: 'member_ids' and 'member_names' cannot be provided at the same time.")
            return False
        if  'policy_ids' in PARAMS and 'policy_names' in PARAMS:
            print("Error: 'policy_ids' and 'policy_names' cannot be provided at the same time.")
            return False
        valid_fields = {'member_ids', 'member_names', 'policy_ids', 'policy_names'}
    

    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True


def filesystems_policiesall(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-systems/policies-all'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }
    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_policiesall_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystems_policiesall_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'member_ids' in PARAMS and 'member_names' in PARAMS:
            print("Error: 'member_ids' and 'member_names' cannot be provided at the same time.")
            return False
        if  'policy_ids' in PARAMS and 'policy_names' in PARAMS:
            print("Error: 'policy_ids' and 'policy_names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'filter', 'limit', 'member_ids', 'member_names', 'offset', 'policy_ids', 'policy_names', 'sort'}
    
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True


def filesystems_users_performance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-systems/users/performance'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }
    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_users_performance_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystems_users_performance_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'file_system_ids' in PARAMS and 'file_system_names' in PARAMS:
            print("Error: 'file_system_ids' and 'file_system_names' cannot be provided at the same time.")
            return False
        if  'uids' in PARAMS and 'user_names' in PARAMS:
            print("Error: 'uids' and 'user_names' cannot be provided at the same time.")
            return False
        valid_fields = {'file_system_ids', 'file_system_names', 'filter', 'limit', 'names', 'sort', 'total_only', 'uids', 'user_names'}
    
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True


def filesystems_locks(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-systems/locks'
    VALIDATE_METHODS =  ['GET', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }    
    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_locks_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystems_locks_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'file_system_ids' in PARAMS and 'file_system_names' in PARAMS:
            print("Error: 'file_system_ids' and 'file_system_names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'client_names', 'file_system_ids', 'file_system_names', 'filter', 'inodes', 'limit', 'names', 'paths'}
    
    elif METHOD in ['DELETE']:
        if 'file_system_ids' in PARAMS and 'file_system_names' in PARAMS:
            print("Error: 'file_system_ids' and 'file_system_names' cannot be provided at the same time.")
            return False
        valid_fields = {'client_names', 'file_system_ids', 'file_system_names', 'inodes', 'names', 'paths', 'recursive'}
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True



def filesystems_locks_clients(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-systems/locks/clients'
    VALIDATE_METHODS =  ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }    
    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_locks_clients_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystems_locks_clients_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'file_system_ids' in PARAMS and 'file_system_names' in PARAMS:
            print("Error: 'file_system_ids' and 'file_system_names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'filter', 'limit'}
    

    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True


    
def filesystems_locks_nlmreclamation(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-systems/locks/nlm-reclamation'
    VALIDATE_METHODS =  ['POST']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }    
    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_locks_nlmreclamation_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystems_locks_nlmreclamation_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['POST']:
        valid_fields = {}
    

    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True

def filesystems_sessions(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-systems/sessions'
    VALIDATE_METHODS =  ['GET', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }    
    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_sessions_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystems_sessions_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        valid_fields = {'continuation_token', 'client_names', 'limit', 'names', 'protocols', 'user_names'}
    
    elif METHOD in ['DELETE']:
        valid_fields = {'client_names', 'disruptive', 'names', 'protocols', 'user_names'}
      

    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True
