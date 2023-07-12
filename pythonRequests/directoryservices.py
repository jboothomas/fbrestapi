import requests
import json
from _sendrequest_ import send_request


def directoryservices(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ## Example application/json payload
    #{
    #  "base_dn": "DC=mycompany,DC=com",
    #  "bind_password": "****",
    #  "bind_user": "CN=John,OU=Users,DC=example,DC=com",
    #  "ca_certificate": {
    #    "id": "string",
    #    "name": "string"
    #  },
    #  "ca_certificate_group": {
    #    "id": "string",
    #    "name": "string"
    #  },
    #  "enabled": true,
    #  "management": {
    #    "user_login_attribute": "userPrincipalName",
    #    "user_object_class": "inetOrgPerson"
    #  },
    #  "nfs": {
    #    "nis_domains": [
    #      "ypdomain"
    #    ],
    #    "nis_servers": [
    #      "181.44.543.12"
    #    ]
    #  },
    #  "smb": {
    #    "join_ou": "OU=my_organizational_unit"
    #  },
    #  "uris": [
    #    "ldaps://ad1.mycompany.com"
    #  ]
    #}

    ENDPOINT = f'api/{API_VERSION}/directory-services'
    VALIDATE_METHODS = ['GET', 'PATCH']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, directoryservices_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def directoryservices_validateparams(METHOD, PARAMS):

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



def directoryservices_roles(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ## Example application/json payload
    #{
    #  "role": {
    #    "id": "string",
    #    "name": "string"
    #  },
    #  "group": "groupOfUsers",
    #  "group_base": "OU=PureGroups,OU=SANManagers"
    #}

    ENDPOINT = f'api/{API_VERSION}/directory-services/roles'
    VALIDATE_METHODS = ['GET', 'PATCH']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, directoryservices_roles_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def directoryservices_roles_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'ids' in PARAMS and 'role_names' in PARAMS:
            print("Error: 'ids' and 'role_names' cannot be provided at the same time.")
            return False
        if 'ids' in PARAMS and 'role_ids' in PARAMS:
            print("Error: 'ids' and 'role_ids' cannot be provided at the same time.")
            return False
        if 'role_ids' in PARAMS and 'role_names' in PARAMS:
            print("Error: 'role_ids' and 'role_names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'filter', 'ids', 'limit', 'offset', 'role_ids', 'role_names', 'sort'}
    elif METHOD in ['PATCH']:
        if 'ids' in PARAMS and 'role_names' in PARAMS:
            print("Error: 'ids' and 'role_names' cannot be provided at the same time.")
            return False
        if 'ids' in PARAMS and 'role_ids' in PARAMS:
            print("Error: 'ids' and 'role_ids' cannot be provided at the same time.")
            return False
        if 'role_ids' in PARAMS and 'role_names' in PARAMS:
            print("Error: 'role_ids' and 'role_names' cannot be provided at the same time.")
            return False
        valid_fields = {'ids', 'role_ids', 'role_names'}
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True


def directoryservices_test(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ## Example applicaiton/json payload
    #{
    #  "base_dn": "DC=mycompany,DC=com",
    #  "bind_password": "****",
    #  "bind_user": "CN=John,OU=Users,DC=example,DC=com",
    #  "ca_certificate": {
    #    "id": "string",
    #    "name": "string"
    #  },
    #  "ca_certificate_group": {
    #    "id": "string",
    #    "name": "string"
    #  },
    #  "enabled": true,
    #  "management": {
    #    "user_login_attribute": "userPrincipalName",
    #    "user_object_class": "inetOrgPerson"
    #  },
    #  "nfs": {
    #    "nis_domains": [
    #      "ypdomain"
    #    ],
    #    "nis_servers": [
    #      "181.44.543.12"
    #    ]
    #  },
    #  "smb": {
    #    "join_ou": "OU=my_organizational_unit"
    #  },
    #  "uris": [
    #    "ldaps://ad1.mycompany.com"
    #  ]
    #}

    ENDPOINT = f'api/{API_VERSION}/directory-services/test'
    VALIDATE_METHODS = ['GET', 'PATCH']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, directoryservices_test_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def directoryservices_test_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'filter', 'ids', 'limit', 'names', 'sort'}
    elif METHOD in ['PATCH']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        valid_fields = {'filter', 'ids', 'names', 'sort'}
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True