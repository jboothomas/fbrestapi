from _sendrequest_ import send_request



def logout(FB_IP, X_AUTH_TOKEN, VALIDATE_SSL):

    ENDPOINT = 'api/logout'
    VALIDATE_METHODS = ['POST']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, 'POST', HEADERS, '', '', VALIDATE_METHODS, VALIDATE_SSL)
    return result