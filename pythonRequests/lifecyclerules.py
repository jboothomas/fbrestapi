from _sendrequest_ import send_request


def lifecyclerules(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload
    #{
    #  "abort_incomplete_multipart_uploads_after": 86400000,
    #  "keep_current_version_for": 86400000,
    #  "keep_current_version_until": 1636588800000
    #}

    ENDPOINT = f'api/{API_VERSION}/lifecycle-rules'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result