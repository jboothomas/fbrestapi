from _sendrequest_ import send_request


def snmpmanagers(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):

    #Example application/json payload:
    #{
    #  "name": "string",
    #  "host": "snmp.purestorage.com",
    #  "notification": "trap",
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
    
    ENDPOINT = f'api/{API_VERSION}/snmp-managers'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def snmpmanagers_test(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    ENDPOINT = f'api/{API_VERSION}/snmp-managers/test'
    VALIDATE_METHODS = ['GET']
    HEADERS = {
        'x-auth-token': X_AUTH_TOKEN
    }

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result