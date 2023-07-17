from _sendrequest_ import send_request


def apiversion(FB_IP, VALIDATE_SSL):
    ENDPOINT = 'api/api_version'
    METHOD = 'GET'
    HEADERS = {}
    PARAMS = {}
    PAYLOAD = {}
    VALIDATE_METHODS = ['GET']


    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    #API_VERSIONS = result[2]['versions']
    #return API_VERSIONS
    return result