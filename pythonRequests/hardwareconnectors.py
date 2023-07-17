from _sendrequest_ import send_request


def hardwareconnectors(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    # Example applicaiton/json payload:
    #{{
    #  "lane_speed": 10000000000,
    #  "port_count": 1
    #}

    ENDPOINT = f'api/{API_VERSION}/hardware-connectors'
    VALIDATE_METHODS = ['GET', 'PATCH']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def hardwareconnectors_performance(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/hardware-connectors/performance'
    VALIDATE_METHODS = ['GET']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result