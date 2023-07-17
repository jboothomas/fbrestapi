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

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def filesystemreplicalink_policies(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-system-replica-links/policies'
    VALIDATE_METHODS = ['GET', 'POST', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }
    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def filesystemreplicalinks_transfer(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-system-replica-links/transfer'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }    
    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result