from _sendrequest_ import send_request


def smbclientpolicies(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload:
    #{
    #  "name": "string",
    #  "enabled": true,
    #  "rules": [
    #    {
    #      "client": "string",
    #      "permission": "string"
    #    }
    #  ]
    #}

    ENDPOINT = f'api/{API_VERSION}/smb-client-policies'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def smbclientpolicies_rules(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload:
    #{
    #  "client": "1.2.3.4",
    #  "permission": "string",
    #  "index": 0
    #}

    ENDPOINT = f'api/{API_VERSION}/smb-client-policies/rules'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result