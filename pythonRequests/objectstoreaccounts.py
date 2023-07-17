from _sendrequest_ import send_request


def objectstoreaccounts(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example applicaiton/json payload:
    #{{
    # "bucket_defaults": {
    #    "hard_limit_enabled": true,
    #    "quota_limit": "string"
    #  },
    #  "hard_limit_enabled": true,
    #  "quota_limit": "string"
    #}
    
    ENDPOINT = f'api/{API_VERSION}/object-store-accounts'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result