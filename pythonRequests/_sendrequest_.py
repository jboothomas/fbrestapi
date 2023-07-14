import requests
import json

def send_request(FB_IP, ENDPOINT, METHOD, HEADERS, PARAMS, PAYLOAD, validate_func, VALIDATE_METHODS, VALIDATE_SSL):
    url = f"https://{FB_IP}/{ENDPOINT}"

    #print(url)

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
    try:
        response = requests.request(
            METHOD,
            url,
            headers=HEADERS,
            params=PARAMS,
            data=payload,
            verify=VALIDATE_SSL  # consider removing this if your FB has a valid SSL cert
        )
        response.raise_for_status() 

    except requests.exceptions.HTTPError as e:
        # An HTTP error occurred
        print(f'An HTTP error occurred during {METHOD}: {e}')
        data = response.json()
        errormessage = data['errors'][0]['message']
        print(f'RESTAPI error message: {errormessage}')
        return None

    except requests.exceptions.RequestException as e:
        # A network problem occurred
        print(f'A network problem occurred: {e}')
        return None


    else:
        # The request was successful
        #print('The request was successful')
  

        if response.status_code == 200:
            header = response.headers
            try:
                data = response.json()
                return response.status_code, header, data
            except json.JSONDecodeError:
                return response.status_code, header
