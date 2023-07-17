from _sendrequest_ import send_request


def support(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    #Example application/json payload:
    #{
    #  "phonehome_enabled": true,
    #  "proxy": "string",
    #  "remote_assist_active": true
    #}
    
    ENDPOINT = f'api/{API_VERSION}/support'
    VALIDATE_METHODS = ['GET', 'PATCH']


    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def support_test(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    ENDPOINT = f'api/{API_VERSION}/support/test'
    VALIDATE_METHODS = ['GET']


    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result