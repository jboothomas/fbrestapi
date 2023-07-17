from _sendrequest_ import send_request


def bucketreplicalinks(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ## Example application/json payload
    #{
    #  "paused": true,
    #  "remote_credentials": {
    #    "id": "string",
    #    "name": "string"
    #  }
    #}

    ENDPOINT = f'api/{API_VERSION}/bucket-replica-links'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result