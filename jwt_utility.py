import jwt
import base64
import os
from datetime import datetime

def get_secret_key():
    with open('secret.txt', 'r') as file:
        return file.read().strip()

def generate_jwt(data):
    secret = get_secret_key()
    current_time = datetime.utcnow()
    timestamp = int(current_time.timestamp())
    jti = base64.urlsafe_b64encode(os.urandom(16)).rstrip(b'=').decode('utf-8')

    payload = {
        'data': data,
        'date': current_time.strftime('%Y-%m-%d')
    }

    token = jwt.encode(
        {
            'iat': timestamp,
            'jti': jti,
            'payload': payload
        },
        secret,
        algorithm='HS512'
    )

    return token

def validate_jwt(token):
    secret = get_secret_key()

    try:
        decoded_token = jwt.decode(token, secret, algorithms=['HS512'])
        return decoded_token
    except jwt.InvalidTokenError:
        return None

# Usage example
input_data = 'example data'
jwt_token = generate_jwt(input_data)
print(jwt_token)

decoded_token = validate_jwt(jwt_token)
if decoded_token is not None:
    print("JWT is valid!")
    print(decoded_token)
else:
    print("JWT is invalid!")

