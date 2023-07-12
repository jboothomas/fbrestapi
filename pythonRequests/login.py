import requests
from _sendrequest_ import send_request

def login(FB_IP, API_TOKEN, VALIDATE_SSL):

    ENDPOINT = 'api/login'
    VALIDATE_METHODS = ['POST']
    HEADERS = {
        'api-token': API_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, 'POST', HEADERS, '', '', login_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    X_AUTH_TOKEN = result[0].get('X-Auth-Token')
    return X_AUTH_TOKEN


def login_validateparams(METHOD, PARAMS):
    if METHOD in ['POST']:
        valid_fields = {}
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True