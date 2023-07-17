from _sendrequest_ import send_request

def oauth2_token(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload
    #{
    #    'grant_type': 'urn:ietf:params:oauth:grant-type:token-exchange',
    #    'subject_token': 'your_jwt_token',
    #    'subject_token_type': 'urn:ietf:params:oauth:token-type:jwt'
    #}

    ENDPOINT = f'oauth2/1.0/token'
    VALIDATE_METHODS = ['POST']
    HEADERS = {
         'Content-Type': 'application/x-www-form-urlencoded',
         'Accept': 'application/json'
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result