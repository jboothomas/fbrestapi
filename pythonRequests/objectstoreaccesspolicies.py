from _sendrequest_ import send_request


def objectstoreaccesspolicies(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload:
    #null

    ENDPOINT = f'api/{API_VERSION}/object-store-access-policies'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def objectstoreaccesspolicies_objectstoreusers(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload:
    #

    ENDPOINT = f'api/{API_VERSION}/object-store-policies/object-store-users'
    VALIDATE_METHODS = ['GET', 'POST', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result

def objectstoreaccesspolicies_rules(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):
    
    #Example application/json payload:
    #{
    #  "actions": [
    #    "s3:CreateBucket",
    #    "s3:PutObject"
    #  ],
    #  "conditions": {
    #    "source_ips": [
    #      "1.2.3.4",
    #      "5.6.7.0/24",
    #      "2001:DB8:1234:5678::/64"
    #    ],
    #    "s3_delimiters": [
    #      "/"
    #    ],
    #    "s3_prefixes": [
    #      "home/"
    #    ]
    #  },
    #  "resources": [
    #    "*",
    #    "mybucket",
    #    "mybucket*",
    #    "mybucket*/myobject*"
    #  ]
    #}

    ENDPOINT = f'api/{API_VERSION}/object-store-policies/rules'
    VALIDATE_METHODS = ['GET', 'POST', 'PATCH', 'DELETE']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result