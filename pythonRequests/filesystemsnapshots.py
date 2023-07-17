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

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def filesystemsnapshots_policies(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-system-snapshots/policies'
    VALIDATE_METHODS = ['GET', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }
    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def filesystemsnapshots_transfer(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/file-systemsnapshots/transfer'
    VALIDATE_METHODS = ['GET', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }    
    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result