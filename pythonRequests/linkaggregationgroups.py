from _sendrequest_ import send_request


def linkaggregationgroups(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload
    #{
    #  "ports": [
    #    {
    #      "name": "string"
    #    }
    #  ],
    #  "add_ports": [
    #    {
    #      "name": "string"
    #    }
    #  ],
    #  "remove_ports": [
    #    {
    #      "name": "string"
    #    }
    #  ]
    #}

    ENDPOINT = f'api/{API_VERSION}/link-aggregation-groups'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result