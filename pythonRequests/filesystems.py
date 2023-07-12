import requests
import json
from _sendrequest_ import send_request


def filesystems(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ## Example application/json payload
    #{
    #  "default_group_quota": 0,
    #  "default_user_quota": 0,
    #  "destroyed": true,
    #  "fast_remove_directory_enabled": true,
    #  "hard_limit_enabled": true,
    #  "http": {
    #    "enabled": true
    #  },
    #  "multi_protocol": {
    #    "access_control_style": "string",
    #    "safeguard_acls": true
    #  },
    #  "nfs": {
    #    "v3_enabled": true,
    #    "v4_1_enabled": true,
    #    "rules": "1.0.0.0/8(rw,no_root_squash) fd01:abcd::/64(ro,secure,root_squash,anongid=16000) @netgrp(rw,all_squash,anonuid=99,fileid_32bit) 1.41.8.32(rw,no_all_squash,sec=krb5:krb5i:krp5p) my-hostname(rw,no_root_squash) host.exampledomain.com(rw,no_root_squash) host?(rw,no_root_squash) host?.example*domain.com(rw,no_root_squash) host.*(rw,no_root_squash)",
    #    "add_rules": "string",
    #    "remove_rules": "string",
    #    "after": "string",
    #    "export_policy": {
    #      "id": "string",
    #      "name": "string"
    #    }
    #  },
    #  "provisioned": 1048576,
    #  "requested_promotion_state": "string",
    #  "smb": {
    #    "enabled": true,
    #    "client_policy": {
    #      "id": "string",
    #      "name": "string"
    #    },
    #    "share_policy": {
    #      "id": "string",
    #      "name": "string"
    #    }
    #  },
    #  "snapshot_directory_enabled": true,
    #  "source": {
    #    "id": "string",
    #    "name": "string",
    #    "location": {
    #      "id": "string",
    #      "name": "string"
    #    }    
    #  },
    #  "space": {},
    #  "writable": true
    #}
    ENDPOINT = f'api/{API_VERSION}/file-systems'
    VALIDATE_METHODS = ['GET', 'POST', 'DELETE', 'PATCH']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystems_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'destroyed', 'filter', 'ids', 'limit', 'names', 'offset', 'sort', 'total_only'}
    
    elif METHOD in ['POST']:
        valid_fields = {'discard_non_snapshotted_data', 'names', 'overwrite'}

    elif METHOD in ['DELETE']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'ids', 'names'}
    
    elif METHOD in ['PATCH']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'delete_link_on_eradication', 'discard_detailed_permissions', 'discard_non_snapshotted_data', 'ids', 'ignore_usage', 'names'}

    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True


def filesystems_groups_performance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-systems/groups/performance'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_groups_performance_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystems_groups_performance_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'gids' in PARAMS and 'group_names' in PARAMS:
            print("Error: 'gids' and 'group_names' cannot be provided at the same time.")
            return False
        valid_fields = {'file_system_ids', 'file_system_names', 'filter', 'gids', 'group_names', 'limit', 'names', 'sort', 'total_only'}
    
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True

def filesystems_performance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-systems/performance'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }    
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_performance_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystems_performance_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        valid_fields = {'continuation_token', 'end_time', 'filter', 'ids', 'limit', 'names', 'offset', 'protocol', 'resolution', 'sort', 'start_time', 'total_only'}
    
    
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
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_policies_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
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
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_policiesall_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
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
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_users_performance_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
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
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_locks_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
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
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_locks_clients_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
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
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_locks_nlmreclamation_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
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
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystems_sessions_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
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
