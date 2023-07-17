from _sendrequest_ import send_request


def usage_groups(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    ENDPOINT = f'api/{API_VERSION}/usage/groups'
    VALIDATE_METHODS = ['GET']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def usage_users(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/usage/users'
    VALIDATE_METHODS = ['GET']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result