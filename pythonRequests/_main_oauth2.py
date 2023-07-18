from oauth2 import oauth2_token
from _jwt_ import create_jwt
from apiversion import apiversion
from arrays import arrays
from drives import drives


def main():
    FB_IP = '<YOUR_FLASHBLADE_IP>'
    API_TOKEN = '<YOUR_FB_API_TOKEN>'

    ## Provide oauth2 parameters
    kid_input = "kid_value"
    sub_input = "sub_value"
    issuer_input = "issuer_value"
    aud_input = "aud_valuef"
    private_key = """
-----BEGIN RSA PRIVATE KEY-----
abcdef
-----END RSA PRIVATE KEY-----
"""
    jwt = create_jwt(kid_input, sub_input, issuer_input, aud_input, private_key)
    print(jwt)

    payload = {
        'grant_type': 'urn:ietf:params:oauth:grant-type:token-exchange',
        'subject_token': jwt,
        'subject_token_type': 'urn:ietf:params:oauth:token-type:jwt'
    }

    ## Authenticate with FlashBlade 
    POST_OAUTH2 = oauth2_token('POST', FB_IP, payload, False )
  

    if POST_OAUTH2 is not None:
        BEARER_TOKEN = POST_OAUTH2[2]['access_token']
        print(f'Login succesfull received x-auth-token: {BEARER_TOKEN}')

        # Get latest API version
        GET_API_VERSIONS = apiversion(FB_IP, False)
        if GET_API_VERSIONS is not None:
            API_VERSION = GET_API_VERSIONS[2]['versions'][-1]
            print(f'RestAPI version will be: {API_VERSION}')
        else:
            print('Failed to get api versions')
    
        HEADERS = {
            'Authorization': 'Bearer ' + BEARER_TOKEN
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

    else:
        print("Failed to authenticate")


if __name__ == "__main__":
    main()