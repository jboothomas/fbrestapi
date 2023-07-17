from _sendrequest_ import send_request


def arrayconnections(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ## Example application/json payload
    #{{
    #  "encrypted": true,
    #  "management_address": "10.202.101.78",
    #  "replication_addresses": [
    #    "10.202.101.70"
    #  ],
    #  "throttle": {
    #    "default_limit": 1073741824,
    #    "window": {
    #      "start": 3600000,
    #      "end": 46800000
    #    },
    #    "window_limit": 2097152
    #  }
    #}

    ENDPOINT =  f'api/{API_VERSION}/array-connections'
    VALIDATE_METHODS = ['GET', 'PATCH', 'POST', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def arrayconnections_connectionkey(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    ## Example application/json payload
    #{
    #  "items": [
    #    {
    #      "connection_key": "6207d123-d123-0b5c-5fa1-95fabc5c7123",
    #      "created": 0,
    #      "expires": 0
    #    }
    #  ]
    #}
    ENDPOINT =  f'api/{API_VERSION}/array-connections/connection-key'
    VALIDATE_METHODS = ['GET', 'POST']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def arrayconnections_path(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    ENDPOINT =  f'api/{API_VERSION}/array-connections/path'
    VALIDATE_METHODS = ['GET']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def arrayconnections_performance_replication(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT =  f'api/{API_VERSION}/array-connections/performance/replication'
    VALIDATE_METHODS = ['GET']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result
