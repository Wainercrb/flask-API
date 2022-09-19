import os
from utils.jwt_token import generate_token
from utils.password_encryption import generate_payload


def test_validate_generate_jwt_token():
    secret = os.environ.get('TOKEN_SECRET')
    user = {'id': '123456789',
            'name': 'test test test',
            'email': 'test@gmail.com',
            'password': 'test1234'}
    payload = generate_payload(user)
    token = generate_token(payload, secret)

    assert type(token) is str
    assert len(token) > 10


def test_validate_jwt_token_wrong_payload():
    try:
        secret = os.environ.get('TOKEN_SECRET')
        user = {'name': 'test test test',
                'email': 'test@gmail.com',
                'password': 'test1234'}

        payload = generate_payload(user)
        _ = generate_token(payload, secret)
    except Exception as e:
        assert type(e) is KeyError
