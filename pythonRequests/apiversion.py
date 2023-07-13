from _sendrequest_ import send_request


def apiversion(FB_IP, VALIDATE_SSL):
    ENDPOINT = 'api/api_version'
    METHOD = 'GET'
    HEADERS = {}
    PARAMS = {}
    PAYLOAD = {}
    VALIDATE_METHODS = ['GET']


    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, apiversion_validateparams, VALIDATE_METHODS, VALIDATE_SSL)
    #API_VERSIONS = result[2]['versions']
    #return API_VERSIONS
    return result

def apiversion_validateparams(METHOD, PARAMS):
    if METHOD in ['GET']:
        valid_fields = {}
    # Check if any field in params is not in possible_fields
    for field in PARAMS:
        if field not in valid_fields:
            print(f"Error: Unknown field '{field}'.")
            return False

    # If no errors were found, the params are valid
    return True
