from _sendrequest_ import send_request


def filesystemreplicalinks(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

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
    ENDPOINT = f'api/{API_VERSION}/file-system-replica-links'
    VALIDATE_METHODS = ['GET', 'POST', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystemreplicalinks_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystemreplicalinks_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'ids' in PARAMS and 'names' in PARAMS:
            print("Error: 'ids' and 'names' cannot be provided at the same time.")
            return False
        if 'local_file_system_ids' in PARAMS and 'local_file_system_names' in PARAMS:
            print("Error: 'local_file_system_ids' and 'local_file_system_names' cannot be provided at the same time.")
            return False
        if 'remote_file_system_ids' in PARAMS and 'remote_file_system_names' in PARAMS:
            print("Error: 'remote_file_system_ids' and 'remote_file_system_names' cannot be provided at the same time.")
            return False
        if 'remote_ids' in PARAMS and 'remote_names' in PARAMS:
            print("Error: 'remote_ids' and 'remote_names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'filter', 'ids', 'limit', 'local_file_system_ids', 'local_file_system_names', 'offset', 'remote_file_syste_ids', 'remote_file_system_names', 'remote_ids', 'remote_names', 'sort'}
    
    elif METHOD in ['POST']:
        if 'local_file_system_ids' in PARAMS and 'local_file_system_names' in PARAMS:
            print("Error: 'local_file_system_ids' and 'local_file_system_names' cannot be provided at the same time.")
            return False
        if 'remote_file_system_ids' in PARAMS and 'remote_file_system_names' in PARAMS:
            print("Error: 'remote_file_system_ids' and 'remote_file_system_names' cannot be provided at the same time.")
            return False
        if 'remote_ids' in PARAMS and 'remote_names' in PARAMS:
            print("Error: 'remote_ids' and 'remote_names' cannot be provided at the same time.")
            return False
        valid_fields = {'ids', 'local_file_system_ids', 'local_file_system_names', 'remote_file_system_names', 'remote_ids', 'remote_names'}

    elif METHOD in ['DELETE']:
        if 'local_file_system_ids' in PARAMS and 'local_file_system_names' in PARAMS:
            print("Error: 'local_file_system_ids' and 'local_file_system_names' cannot be provided at the same time.")
            return False
        if 'remote_file_system_ids' in PARAMS and 'remote_file_system_names' in PARAMS:
            print("Error: 'remote_file_system_ids' and 'remote_file_system_names' cannot be provided at the same time.")
            return False
        if 'remote_ids' in PARAMS and 'remote_names' in PARAMS:
            print("Error: 'remote_ids' and 'remote_names' cannot be provided at the same time.")
            return False
        valid_fields = {'ids', 'local_file_system_ids', 'local_file_system_names', 'remote_file_system_names', 'remote_ids', 'remote_names', 'cancel_in_progress_transfers'}
    
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


def filesystemreplicalink_policies(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-system-replica-links/policies'
    VALIDATE_METHODS = ['GET', 'POST', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }
    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystemreplicalink_policies_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystemreplicalink_policies_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'local_file_system_ids' in PARAMS and 'local_file_system_names' in PARAMS:
            print("Error: 'local_file_system_ids' and 'local_file_system_names' cannot be provided at the same time.")
            return False
        if 'policy_ids' in PARAMS and 'policy_names' in PARAMS:
            print("Error: 'policy_ids' and 'policy_names' cannot be provided at the same time.")
            return False
        if 'remote_ids' in PARAMS and 'remote_names' in PARAMS:
            print("Error: 'remote_ids' and 'remote_names' cannot be provided at the same time.")
            return False
        if 'remote_file_system_ids' in PARAMS and 'remote_file_system_names' in PARAMS:
            print("Error: 'remote_file_system_ids' and 'remote_file_system_names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'filter', 'limit', 'local_file_system_ids', 'local_file_system_names', 'member_ids', 'offset', 'policy_ids', 'policy_names', 'remote_ids', 'remote_file_system_ids', 'remote_file_system_names', 'remote_names', 'sort'}
    elif METHOD in ['POST', 'DELETE']:
        if 'local_file_system_ids' in PARAMS and 'local_file_system_names' in PARAMS:
            print("Error: 'local_file_system_ids' and 'local_file_system_names' cannot be provided at the same time.")
            return Flashe
        if 'policy_ids' in PARAMS and 'policy_names' in PARAMS:
            print("Error: 'policy_ids' and 'policy_names' cannot be provided at the same time.")
            return False
        if 'remote_ids' in PARAMS and 'remote_names' in PARAMS:
            print("Error: 'remote_ids' and 'remote_names' cannot be provided at the same time.")
            return False
        valid_fields = {'local_file_system_ids', 'local_file_system_names', 'member_ids', 'policy_ids', 'policy_names', 'remote_ids', 'remote_names',}
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True

def filesystemreplicalinks_transfer(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-system-replica-links/transfer'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }    
    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, filesystemreplicalinks_transfer_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystemreplicalinks_transfer_validateparams(METHOD, PARAMS):

    # Define the set of all possible fields based on method
    if METHOD in ['GET']:
        if 'remote_ids' in PARAMS and 'remote_names' in PARAMS:
            print("Error: 'remote_ids' and 'remote_names' cannot be provided at the same time.")
            return False
        valid_fields = {'continuation_token', 'filter', 'ids', 'limit', 'names_or_owner_names', 'offset', 'remote_ids', 'remote_names', 'sort', 'total_only'}
    
    
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True