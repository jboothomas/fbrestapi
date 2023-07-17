from _sendrequest_ import send_request


def smtpservers(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    #Example application/json payload:
    #{
    #  "relay_host": "string",
    #  "sender_domain": "string"
    #}
    
    ENDPOINT = f'api/{API_VERSION}/smtp-servers'
    VALIDATE_METHODS = ['GET', 'PATCH']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result