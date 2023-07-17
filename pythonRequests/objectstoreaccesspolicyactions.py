from _sendrequest_ import send_request


def objectstoreaccesspolicyactions(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload:
    #null

    ENDPOINT = f'api/{API_VERSION}/object-store-access-policy-actions'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result