import requests
import json


def directoryservices(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

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

    url = f"https://{FB_IP}/api/{API_VERSION}/directory-services"
    
    if METHOD not in ['GET', 'PATCH']:
        print(f'The method "{METHOD}" is not valid for {url}.')
        return
    
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }
    # Convert payload to JSON
    payload = json.dumps(PAYLOAD)

    response = requests.request(
        METHOD,
        url, 
        headers=headers, 
        data=payload,
        verify=False  # consider removing this if your FB has a valid SSL cert
    )

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'{METHOD} request to {url} failed with status code {response.status_code}')
        return None

def directoryservices_roles(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

    ## Example application/json payload
    #{
    #  "role": {
    #    "id": "string",
    #    "name": "string"
    #  },
    #  "group": "groupOfUsers",
    #  "group_base": "OU=PureGroups,OU=SANManagers"
    #}

    url = f"https://{FB_IP}/api/{API_VERSION}/directory-services/roles"
    
    if METHOD not in ['GET', 'PATCH']:
        print(f'The method "{METHOD}" is not valid for {url}.')
        return
    
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }
    # Convert payload to JSON
    payload = json.dumps(PAYLOAD)

    response = requests.request(
        METHOD,
        url, 
        headers=headers, 
        data=payload,
        verify=False  # consider removing this if your FB has a valid SSL cert
    )

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'{METHOD} request to {url} failed with status code {response.status_code}')
        return None

def directoryservices_test(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):

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

    url = f"https://{FB_IP}/api/{API_VERSION}/directory-services/test"
    
    if METHOD not in ['GET', 'PATCH']:
        print(f'The method "{METHOD}" is not valid for {url}.')
        return
    
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }
    # Convert payload to JSON
    payload = json.dumps(PAYLOAD)

    response = requests.request(
        METHOD,
        url, 
        headers=headers, 
        data=payload,
        verify=False  # consider removing this if your FB has a valid SSL cert
    )

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'{METHOD} request to {url} failed with status code {response.status_code}')
        return None