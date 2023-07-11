from login import login
from logout import logout
from api_version import api_version

FB_IP = '<YOUR_FLASHBLADE_IP>'
API_TOKEN = '<YOUR_FB_API_TOKEN>'
#USER = '<YOUR_USERNAME>'
#PASSWORD = '<YOUR_PASSWORD>'

token = login(FB_IP, API_TOKEN)

if token is not None:
    print(f'Login succesfull received x-auth-token: {token}')

    # Get latest api_version
    versions = api_version(FB_IP)
    if versions is not None:
        useVersion = versions[-1]
        print(f'RestAPI version will be: {useVersion}')
    else:
        print('Failed to get api versions')

    # Use the token to logout
    logout_status = logout(FB_IP, token)
    print(logout_status)



else:
    print("Failed to authenticate")