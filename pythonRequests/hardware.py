from _sendrequest_ import send_request


def hardware(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    # Example applicaiton/json payload:
    #{
    #  "identify_enabled": true
    #}

    ENDPOINT = f'api/{API_VERSION}/hardware'
    VALIDATE_METHODS = ['GET', 'PATCH']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result