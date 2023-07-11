import requests

#FB_IP = '<YOUR_FLASHBLADE_IP>'
FB_IP = '10.225.112.165'
#USER = '<YOUR_USERNAME>'
#PASSWORD = '<YOUR_PASSWORD>'
#API_TOKEN = '<YOUR_FB_API_TOKEN>'
API_TOKEN = 'T-7c7a862d-b636-4966-8a24-f1086ca8f23e'
#API_VERSION = '1.6'  # Make sure to set the appropriate API version for your FlashBlade

def logout(FB_IP, token):

    # Logout using X-Auth-Token
    url = f"https://{FB_IP}/api/logout"
    headers = {
      'x-auth-token': token
    }

    logout_response = requests.post(
        url,
        headers=headers,
        verify=False  # consider removing this if your FB has a valid SSL cert
    )

    if logout_response.status_code == 200:
        return(f'Logout succesfull code {logout_response.status_code}')
    else:
        return(f'Logout failed with status code {auth_response.status_code}')
