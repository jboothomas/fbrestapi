import requests

def logout(FB_IP, X_AUTH_TOKEN):

    # Logout using X-Auth-Token
    url = f"https://{FB_IP}/api/logout"
    headers = {
      'x-auth-token': X_AUTH_TOKEN
    }

    response = requests.post(
        url,
        headers=headers,
        verify=False  # consider removing this if your FB has a valid SSL cert
    )

    if response.status_code == 200:
        return(f'Logout succesfull code {response.status_code}')
    else:
        return(f'Logout failed with status code {response.status_code}')
