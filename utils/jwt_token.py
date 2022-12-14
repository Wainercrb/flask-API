import jwt
import os
from flask import make_response, request

secret = os.environ.get('TOKEN_SECRET')

def generate_token(payload, secret):
    return jwt.encode(payload, secret, algorithm="HS256")


def validate_token(func):

    def wrapper(*args, **kwargs):
        try:
            token = request.headers['token']
        except Exception as e:
            return make_response({
                'message': 'Token not provided',
                'exception': str(e)}, 403
            )

        try:
            jwt.decode(token, secret, algorithms=["HS256"])
            return func(*args, **kwargs)
        except Exception as e:
            return make_response({
                'message': 'Invalid token provided',
                'exception': str(e)}, 403
            )
    return
