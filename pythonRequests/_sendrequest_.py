import requests
import json

def send_request(FB_IP, API_VERSION, ENDPOINT, METHOD, PARAMS, PAYLOAD, X_AUTH_TOKEN, validate_func, VALIDATE_METHODS, VALIDATE_SSL):
    url = f"https://{FB_IP}/api/{API_VERSION}/{ENDPOINT}"

    valid_methods = ['GET', 'POST', 'DELETE', 'PATCH']

    if METHOD not in VALIDATE_METHODS:
        print(f'The method "{METHOD}" is not valid for {url}.')
        return

    if not validate_func(METHOD, PARAMS):
        print(f'The parameters for {METHOD} on {url} are not valid.')
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
        params=PARAMS,
        data=payload,
        verify=VALIDATE_SSL  # consider removing this if your FB has a valid SSL cert
    )

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'{METHOD} request to {url} failed with status code {response.status_code} error message: {errormessage}')
        return None