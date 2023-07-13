import requests
import json

def send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, validate_func, VALIDATE_METHODS, VALIDATE_SSL):
    url = f"https://{FB_IP}/{ENDPOINT}"

    #print(url)

    valid_methods = ['GET', 'POST', 'DELETE', 'PATCH']

    if METHOD not in VALIDATE_METHODS:
        print(f'The method "{METHOD}" is not valid for {url}.')
        return

    if not validate_func(METHOD, PARAMS):
        print(f'The parameters for {METHOD} on {url} are not valid.')
        return

    # Convert payload to JSON
    payload = json.dumps(PAYLOAD)

    if not VALIDATE_SSL:
        requests.packages.urllib3.disable_warnings() 

    response = requests.request(
        METHOD,
        url,
        headers=HEADERS,
        params=PARAMS,
        data=payload,
        verify=VALIDATE_SSL  # consider removing this if your FB has a valid SSL cert
    )

    if response.status_code == 200:
        header = response.headers
        try:
            data = response.json()
            return response.status_code, header, data
        except json.JSONDecodeError:
            return response.status_code, header
    else:
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'{METHOD} request to {url} failed with status code {response.status_code} error message: {errormessage}')
        return None