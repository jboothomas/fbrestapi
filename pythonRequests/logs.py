from _sendrequest_ import send_request


def logs(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    

    ENDPOINT = f'api/{API_VERSION}/logs'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def logsasync(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload
    #{
    #  "start_time": 1514764800000,
    #  "end_time": 1514764800000,
    #  "hardware_components": [
    #    {
    #      "name": "string"
    #    }
    #  ]
    #}

    ENDPOINT = f'api/{API_VERSION}/logs-async'
    VALIDATE_METHODS = ['GET', 'PATCH']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def logsasync_download(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/logs-async/download'
    VALIDATE_METHODS = ['GET']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result