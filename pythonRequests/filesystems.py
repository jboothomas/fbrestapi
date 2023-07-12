import requests
import json
from _sendrequest_ import send_request


def filesystems(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD):

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
    ENDPOINT = 'file-systems'
    VALIDATE_METHODS = ['GET', 'POST', 'DELETE', 'PATCH']
    VALIDATE_SSL = False

    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, PARAMS, PAYLOAD, X_AUTH_TOKEN, filesystems_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystems_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD is 'GET':
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'destroyed', 'filter', 'ids', 'limit', 'names', 'offset', 'sort', 'total_only'}
    
    elif METHOD is 'POST':
        valid_fields = {'discard_non_snapshotted_data', 'names', 'overwrite'}

    elif METHOD is 'DELETE':
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'ids', 'names'}
    
    elif METHOD is 'PATCH':
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


def filesystems_groups_performance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    ENDPOINT = "file-systems/groups/performance"
    VALIDATE_METHODS = ['GET']
    VALIDATE_SSL = False
    
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, PARAMS, PAYLOAD, X_AUTH_TOKEN, filesystems_groups_performance_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def filesystems_performance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    ENDPOINT = "file-systems/performance"
    VALIDATE_METHODS = ['GET']
    VALIDATE_SSL = False
    
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, PARAMS, PAYLOAD, X_AUTH_TOKEN, filesystems_performance_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

    

def filesystems_policies(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    ENDPOINT = "file-systems/policies"
    VALIDATE_METHODS = ['GET', 'POST', 'DELETE']
    VALIDATE_SSL = False
    
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, PARAMS, PAYLOAD, X_AUTH_TOKEN, filesystems_policies_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def filesystems_policiesall(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    ENDPOINT = "file-systems/policies-all"
    VALIDATE_METHODS = ['GET']
    VALIDATE_SSL = False
    
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, PARAMS, PAYLOAD, X_AUTH_TOKEN, filesystems_policiesall_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystems_users_performance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    ENDPOINT = "file-systems/users/performance"
    VALIDATE_METHODS = ['GET']
    VALIDATE_SSL = False
    
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, PARAMS, PAYLOAD, X_AUTH_TOKEN, filesystems_users_performance_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystems_locks(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    ENDPOINT = "file-systems/locks"
    VALIDATE_METHODS =  ['GET', 'DELETE']
    VALIDATE_SSL = False
    
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, PARAMS, PAYLOAD, X_AUTH_TOKEN, filesystems_locks_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def filesystems_locks_clients(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    ENDPOINT = "file-systems/locks/clients"
    VALIDATE_METHODS =  ['GET']
    VALIDATE_SSL = False
    
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, PARAMS, PAYLOAD, X_AUTH_TOKEN, filesystems_locks_clients_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

    
def filesystems_locks_nlmreclamation(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    ENDPOINT = "file-systems/locks/nlm-reclamation"
    VALIDATE_METHODS =  ['POST']
    VALIDATE_SSL = False
    
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, PARAMS, PAYLOAD, X_AUTH_TOKEN, filesystems_locks_nlmreclamation_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def filesystems_sessions(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    ENDPOINT = "file-systems/sessions"
    VALIDATE_METHODS =  ['GET', 'DELETE']
    VALIDATE_SSL = False
    
    result = send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, PARAMS, PAYLOAD, X_AUTH_TOKEN, filesystems_sessions_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result
