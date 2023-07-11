from login import login
from logout import logout

FB_IP = '<YOUR_FLASHBLADE_IP>'
API_TOKEN = '<YOUR_FB_API_TOKEN>'
#USER = '<YOUR_USERNAME>'
#PASSWORD = '<YOUR_PASSWORD>'

token = login(FB_IP, API_TOKEN)

if token is not None:
    print(f'Login succesfull received x-auth-token: {token}')
    # Use the token to logout
    logout_status = logout(FB_IP, token)
    print(logout_status)

else:
    print("Failed to authenticate")