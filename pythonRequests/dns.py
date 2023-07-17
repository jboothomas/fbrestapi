from _sendrequest_ import send_request



def dns(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ## Example application/json payload
    #{
    #  "domain": "example.com",
    #  "nameservers": [
    #    "192.168.0.125"
    #  ]
    #}

    ENDPOINT = f'api/{API_VERSION}/dns'
    VALIDATE_METHODS = ['GET', 'PATCH']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result