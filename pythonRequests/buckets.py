from _sendrequest_ import send_request


def buckets(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ##Example application/json payload
    #{
    #  "destroyed": true,
    #  "hard_limit_enabled": true,
    #  "object_lock_config": {
    #    "default_retention_mode": "governance",
    #    "enabled": true,
    #    "freeze_locked_objects": true,
    #    "default_retention": "86400000"
    #  },
    #  "quota_limit": "string",
    #  "retention_lock": "unlocked",
    #  "versioning": "string"
    #}

    ENDPOINT = f'api/{API_VERSION}/buckets'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def buckets_performance(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/buckets/performance'
    VALIDATE_METHODS = ['GET']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def buckets_s3specificperformance(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ENDPOINT = f'api/{API_VERSION}/buckets/s3-specific-performance'
    VALIDATE_METHODS = ['GET']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result