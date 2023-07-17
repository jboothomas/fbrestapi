from _sendrequest_ import send_request


def smbsharepolicies(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload:
    #{
    #  "name": "string",
    #  "enabled": true,
    #  "rules": [
    #    {
    #      "change": "string",
    #      "full_control": "string",
    #      "principal": "string",
    #      "read": "string"
    #    }
    #  ]
    #}

    ENDPOINT = f'api/{API_VERSION}/smb-share-policies'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def smbsharepolicies_rules(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload:
    #{
    #  "change": "string",
    #  "full_control": "string",
    #  "read": "string"
    #}

    ENDPOINT = f'api/{API_VERSION}/smb-share-policies/rules'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result