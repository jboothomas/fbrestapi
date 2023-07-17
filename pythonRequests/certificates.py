from _sendrequest_ import send_request


def certificates(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    ## Example application/json payload
    #{
    #  "certificate": "string",
    #  "intermediate_certificate": "string",
    #  "passphrase": "string",
    #  "private_key": "string"
    #}
    ENDPOINT = f'api/{API_VERSION}/certificates'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def certificates_certificategroups(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/certificates/certificate-groups'
    VALIDATE_METHODS = ['GET', 'POST', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def certificates_uses(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/certificates/uses'
    VALIDATE_METHODS = ['GET']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result