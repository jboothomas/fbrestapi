from _sendrequest_ import send_request

def login(FB_IP, API_TOKEN, VALIDATE_SSL):

    ENDPOINT = 'api/login'
    VALIDATE_METHODS = ['POST']
    HEADERS = {
        'api-token': API_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, 'POST', HEADERS, '', '', VALIDATE_METHODS, VALIDATE_SSL)
    #X_AUTH_TOKEN = result[1].get('X-Auth-Token')
    #return X_AUTH_TOKEN
    return result