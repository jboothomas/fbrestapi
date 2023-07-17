from _sendrequest_ import send_request


def keytabs(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/keytabs'
    VALIDATE_METHODS = ['GET', 'DELETE', 'POST']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def keytabs_download(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/keytabs/download'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def keytabs_upload(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/keytabs/upload'
    VALIDATE_METHODS = ['POST']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result