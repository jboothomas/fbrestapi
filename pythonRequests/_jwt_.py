import jwt
import datetime
import time

def create_jwt(kid_input, sub_input, issuer_input, aud_input, private_key):
    # Prepare header
    headers = {
        "alg": "RS256",
        "typ": "JWT",
        "kid": kid_input
    }
    
    # Get the current time
    current_time_epoch = int(time.time())
    
    # Prepare payload
    payload = {
        "sub": sub_input,
        "iss": issuer_input,
        "aud": aud_input,
        "iat": current_time_epoch,
        "exp": current_time_epoch + datetime.timedelta(days=1).total_seconds() # current time + 1 day
    }
    
    # Encode the JWT
    encoded_jwt = jwt.encode(payload, private_key, algorithm="RS256", headers=headers)
    
    return encoded_jwt