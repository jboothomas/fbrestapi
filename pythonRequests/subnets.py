from _sendrequest_ import send_request


def subnets(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    #Example application/json payload:
    #{
    #  "gateway": "string",
    #  "link_aggregation_group": {
    #    "id": "string",
    #    "name": "string"
    #  },
    #  "mtu": 1280,
    #  "prefix": "string",
    #  "vlan": 0
    #}
    
    ENDPOINT = f'api/{API_VERSION}/subnets'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result