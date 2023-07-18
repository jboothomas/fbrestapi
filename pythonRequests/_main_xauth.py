from login import login
from logout import logout
from apiversion import apiversion
from arrays import arrays
from drives import drives


def main():
    FB_IP = '<YOUR_FLASHBLADE_IP>'
    API_TOKEN = '<YOUR_FB_API_TOKEN>'

    ## Authenticate with FlashBlade 
    POST_LOGIN = login(FB_IP, API_TOKEN, False)

    if POST_LOGIN is not None:
        X_AUTH_TOKEN = POST_LOGIN[1].get('X-Auth-Token')
        print(f'Login succesfull received x-auth-token: {X_AUTH_TOKEN}')

        # Get latest API version
        GET_API_VERSIONS = apiversion(FB_IP, False)
        if GET_API_VERSIONS is not None:
            API_VERSION = GET_API_VERSIONS[2]['versions'][-1]
            print(f'RestAPI version will be: {API_VERSION}')
        else:
            print('Failed to get api versions')
    
        HEADERS = {
             'x-auth-token': X_AUTH_TOKEN
        }

        # Get array information
        GET_ARRAYS = arrays('GET', FB_IP, API_VERSION, HEADERS, '', '', False)
        if GET_ARRAYS is not None:
            ARRAY_NAME = GET_ARRAYS[2]['items'][0]['name'] ## example to get the array name
            print(ARRAY_NAME)
        else:
            print('Failed to get arrays')

        ## Patch arrays
        ## example patch arrays payload
        patch_arrays_payload = {
            "banner": "" 
        }
        PATCH_ARRAYS = arrays('PATCH', FB_IP, API_VERSION, HEADERS, '', patch_arrays_payload, False)
        if PATCH_ARRAYS is not None:
            print(PATCH_ARRAYS[0])
        else:
            print('Failed to patch arrays')
        
        params = {
        }

        ## Example call and return elements
        METHOD_ELEMENT = drives('GET', FB_IP, API_VERSION, HEADERS, params, '', False )
        if METHOD_ELEMENT is not None:
            print(f'Status code: {METHOD_ELEMENT[0]}')
            print(f'Header: {METHOD_ELEMENT[1]}')
            print(f'Data: {METHOD_ELEMENT[2]}')
            
            
        else:
            print('failed')
        
        # Clear authentication token
        logout_status = logout(FB_IP, X_AUTH_TOKEN, False)
        print(f'logout completed with status code: {logout_status[0]}')

    else:
        print("Failed to authenticate")


if __name__ == "__main__":
    main()