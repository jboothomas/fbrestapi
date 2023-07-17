from _sendrequest_ import send_request


def nfsexportpolicies(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload:
    #{
    #  "name": "string",
    #  "enabled": true,
    #  "rules": [
    #    {
    #      "access": "string",
    #      "anongid": 65530,
    #      "anonuid": 65530,
    #      "atime": true,
    #      "client": "string",
    #      "fileid_32bit": true,
    #      "permission": "string",
    #      "secure": true,
    #      "security": [
    #        "sys"
    #      ]
    #    }
    #  ]
    #}

    ENDPOINT = f'api/{API_VERSION}/nfs-export-policies'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def nfsexportpolicies_rules(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload:
    #{
    #  "access": "string",
    #  "anongid": 65530,
    #  "anonuid": 65530,
    #  "atime": true,
    #  "client": "string",
    #  "fileid_32bit": true,
    #  "permission": "string",
    #  "secure": true,
    #  "security": [
    #    "sys"
    #  ],
    #  "index": 0
    #}

    ENDPOINT = f'api/{API_VERSION}/nfs-export-policies/rules'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result