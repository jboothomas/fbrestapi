from _sendrequest_ import send_request


def kmip(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload
    #{
    #  "uris": [
    #    "my1.kmipserver.com:5696",
    #    "tls://my2.kmipserver.com:5696"
    #  ],
    #  "ca_certificate": {
    #    "id": "string",
    #    "name": "string"
    #  },
    #  "ca_certificate_group": {
    #    "id": "string",
    #    "name": "string"
    #  }
    #}

    ENDPOINT = f'api/{API_VERSION}/kmip'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def kmip_test(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/kmip/test'
    VALIDATE_METHODS = ['GET']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result