import requests
from _sendrequest_ import send_request



def logout(FB_IP, X_AUTH_TOKEN, VALIDATE_SSL):

    ENDPOINT = 'api/logout'
    VALIDATE_METHODS = ['POST']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, 'POST', HEADERS, '', '', logout_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def logout_validateparams(METHOD, PARAMS):
    if METHOD in ['POST']:
        valid_fields = {}
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True