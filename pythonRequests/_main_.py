from login import login
from logout import logout
from api_version import api_version
from arrays import get_arrays

FB_IP = '<YOUR_FLASHBLADE_IP>'
API_TOKEN = '<YOUR_FB_API_TOKEN>'
#USER = '<YOUR_USERNAME>'
#PASSWORD = '<YOUR_PASSWORD>'

X_AUTH_TOKEN = login(FB_IP, API_TOKEN)

if X_AUTH_TOKEN is not None:
    print(f'Login succesfull received x-auth-token: {X_AUTH_TOKEN}')

    # Get latest api_version
    GET_API_VERSIONS = api_version(FB_IP)
    if GET_API_VERSIONS is not None:
        API_VERSION = GET_API_VERSIONS[-1]
        print(f'RestAPI version will be: {API_VERSION}')
    else:
        print('Failed to get api versions')
    
    # Get array information
    GET_ARRAYS = get_arrays(FB_IP, X_AUTH_TOKEN, API_VERSION)
    if GET_ARRAYS is not None:
        #print(GET_ARRAYS)
        ARRAY_NAME = GET_ARRAYS['items'][0]['name'] ## example to get the array name
        print(ARRAY_NAME)
    else:
        print('Failed to get arrays')


    # Use the token to logout
    logout_status = logout(FB_IP, X_AUTH_TOKEN)
    print(logout_status)



else:
    print("Failed to authenticate")