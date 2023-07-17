from _sendrequest_ import send_request


def directoryservices(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ## Example application/json payload
    #{
    #  "base_dn": "DC=mycompany,DC=com",
    #  "bind_password": "****",
    #  "bind_user": "CN=John,OU=Users,DC=example,DC=com",
    #  "ca_certificate": {
    #    "id": "string",
    #    "name": "string"
    #  },
    #  "ca_certificate_group": {
    #    "id": "string",
    #    "name": "string"
    #  },
    #  "enabled": true,
    #  "management": {
    #    "user_login_attribute": "userPrincipalName",
    #    "user_object_class": "inetOrgPerson"
    #  },
    #  "nfs": {
    #    "nis_domains": [
    #      "ypdomain"
    #    ],
    #    "nis_servers": [
    #      "181.44.543.12"
    #    ]
    #  },
    #  "smb": {
    #    "join_ou": "OU=my_organizational_unit"
    #  },
    #  "uris": [
    #    "ldaps://ad1.mycompany.com"
    #  ]
    #}

    ENDPOINT = f'api/{API_VERSION}/directory-services'
    VALIDATE_METHODS = ['GET', 'PATCH']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def directoryservices_roles(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ## Example application/json payload
    #{
    #  "role": {
    #    "id": "string",
    #    "name": "string"
    #  },
    #  "group": "groupOfUsers",
    #  "group_base": "OU=PureGroups,OU=SANManagers"
    #}

    ENDPOINT = f'api/{API_VERSION}/directory-services/roles'
    VALIDATE_METHODS = ['GET', 'PATCH']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result


def directoryservices_test(METHOD, FB_IP, API_VERSION, HEADERS, PARAMS, PAYLOAD, VALIDATE_SSL):

    ## Example applicaiton/json payload
    #{
    #  "base_dn": "DC=mycompany,DC=com",
    #  "bind_password": "****",
    #  "bind_user": "CN=John,OU=Users,DC=example,DC=com",
    #  "ca_certificate": {
    #    "id": "string",
    #    "name": "string"
    #  },
    #  "ca_certificate_group": {
    #    "id": "string",
    #    "name": "string"
    #  },
    #  "enabled": true,
    #  "management": {
    #    "user_login_attribute": "userPrincipalName",
    #    "user_object_class": "inetOrgPerson"
    #  },
    #  "nfs": {
    #    "nis_domains": [
    #      "ypdomain"
    #    ],
    #    "nis_servers": [
    #      "181.44.543.12"
    #    ]
    #  },
    #  "smb": {
    #    "join_ou": "OU=my_organizational_unit"
    #  },
    #  "uris": [
    #    "ldaps://ad1.mycompany.com"
    #  ]
    #}

    ENDPOINT = f'api/{API_VERSION}/directory-services/test'
    VALIDATE_METHODS = ['GET', 'PATCH']

    result = send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, VALIDATE_METHODS, VALIDATE_SSL)
    return result