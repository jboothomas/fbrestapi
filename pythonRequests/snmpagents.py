from _sendrequest_ import send_request


def snmpagents(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    #Example application/json payload:
    #{
    #  "version": "v3",
    #  "v2c": {
    #    "community": "****"
    #  },
    #  "v3": {
    #    "auth_passphrase": "****",
    #    "auth_protocol": "MD5",
    #    "privacy_passphrase": "****",
    #    "privacy_protocol": "DES",
    #    "user": "User1"
    #  }
    #}
    
    ENDPOINT = f'api/{API_VERSION}/snmp-agents'
    VALIDATE_METHODS = ['GET', 'PATCH']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def snmpagents_mib(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    ENDPOINT = f'api/{API_VERSION}/snmp-agents/mib'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result