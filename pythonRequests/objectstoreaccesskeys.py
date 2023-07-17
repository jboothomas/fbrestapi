from _sendrequest_ import send_request


def objectstoreaccesskeys(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example applicaiton/json payload:
    #{
    #  "enabled": true
    #}

    ENDPOINT = f'api/{API_VERSION}/object-store-access-keys'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result