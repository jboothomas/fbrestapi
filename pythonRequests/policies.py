from _sendrequest_ import send_request


def policies(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload:
    #{
    #  "name": "string",
    #  "enabled": true,
    #  "rules": [
    #    {
    #      "at": 0,
    #      "every": 0,
    #      "keep_for": 0,
    #      "time_zone": "America/Los_Angeles"
    #    }
    #  ]
    #}

    ENDPOINT = f'api/{API_VERSION}/policies'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def policies_filesystems(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload:
    #{
    #  "items": [
    #    {
    #      "policy": {
    #        "id": "string",
    #        "name": "string",
    #        "resource_type": "string"
    #      },
    #      "member": {
    #        "id": "string",
    #        "name": "string",
    #        "resource_type": "string"
    #      }
    #    }
    #  ]
    #}

    ENDPOINT = f'api/{API_VERSION}/policies/file-systems'
    VALIDATE_METHODS = ['GET', 'POST', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def policies_filesystemsnapshots(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/policies/file-system-snapshots'
    VALIDATE_METHODS = ['GET', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def policies_members(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/policies/members'
    VALIDATE_METHODS = ['GET']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def policies_filesystemreplicalinks(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/policies/file-system-replica-links'
    VALIDATE_METHODS = ['GET', 'POST', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result