from _sendrequest_ import send_request


def objectstoreremotecredentials(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example applicaiton/json payload:
    #{
    #  "name": "string",
    #  "access_key_id": "PSFBIKZFCAAAKOEJ",
    #  "secret_access_key": "0BEC00003+b1228C223c0FbF1ab5e4GICJGBPJPEOLJCD"
    #}
    
    ENDPOINT = f'api/{API_VERSION}/object-store-remote-credentials'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result