import jwt


headers = {
    'alg': 'HS256',
    'type': 'JWT'
}

payload = {
    'username': 'tester_user',
    'email': 'tester@gmail.com',
    'is_active': False
}

secret = 'secret_123'

token = jwt.encode(headers=headers, payload=payload, key=secret)
print(token)

try:
    decoded_token = jwt.decode(token, secret, algorithms='HS256')
    print(decoded_token)
except jwt.InvalidTokenError:
    print('Invalid token')




