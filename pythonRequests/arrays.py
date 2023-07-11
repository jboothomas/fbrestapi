import requests
import json


def arrays(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):
    ## Example application/json payload
    #{
    #  "name": "string",
    #  "banner": "Restricted area. Authorized personnel only.",
    #  "idle_timeout": 300000,
    #  "ntp_servers": [
    #    "time.acme.com"
    #  ],
    #  "time_zone": "America/Los_Angeles"
    #}

    url = f"https://{FB_IP}/api/{API_VERSION}/arrays"
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


def arrays_eula(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):
    ## Example application/json payload
    #{
    #  "signature": {
    #    "name": "Nice Guy",
    #    "title": "Admin",
    #    "company": "Pure Storage Inc."
    #  }
    #}
   
    url = f"https://{FB_IP}/api/{API_VERSION}/arrays/eula"
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
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'{METHOD} request to {url} failed with status code {response.status_code} error message: {errormessage}')
        return None

def arrays_factoryresettoken(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):
    url = f"https://{FB_IP}/api/{API_VERSION}/arrays/factory-reset-token"
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }

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
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'{METHOD} request to {url} failed with status code {response.status_code} error message: {errormessage}')
        return None

def arrays_httpspecificperformance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):
    url = f"https://{FB_IP}/api/{API_VERSION}/arrays/http-specific-performance"
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }

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
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'{METHOD} request to {url} failed with status code {response.status_code} error message: {errormessage}')
        return None

def arrays_nfsspecificperformance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):
    url = f"https://{FB_IP}/api/{API_VERSION}/arrays/nfs-specific-performance"
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }

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
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'{METHOD} request to {url} failed with status code {response.status_code} error message: {errormessage}')
        return None

def arrays_performance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):
    url = f"https://{FB_IP}/api/{API_VERSION}/arrays/performance"
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }

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
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'{METHOD} request to {url} failed with status code {response.status_code} error message: {errormessage}')
        return None

def arrays_performance_replication(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):
    url = f"https://{FB_IP}/api/{API_VERSION}/arrays/performance/replication"
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }

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
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'{METHOD} request to {url} failed with status code {response.status_code} error message: {errormessage}')
        return None

def arrays_s3specificperformance(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):
    url = f"https://{FB_IP}/api/{API_VERSION}/arrays/s3-specific-performance"
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }

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
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'{METHOD} request to {url} failed with status code {response.status_code} error message: {errormessage}')
        return None

def arrays_space(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):
    url = f"https://{FB_IP}/api/{API_VERSION}/arrays/space"
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }

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
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'{METHOD} request to {url} failed with status code {response.status_code} error message: {errormessage}')
        return None

def arrays_supportedtimezones(METHOD, FB_IP, X_AUTH_TOKEN, API_VERSION, PAYLOAD):
    url = f"https://{FB_IP}/api/{API_VERSION}/arrays/supported-time-zones"
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }

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
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'{METHOD} request to {url} failed with status code {response.status_code} error message: {errormessage}')
        return None