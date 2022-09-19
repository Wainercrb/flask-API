import datetime
from utils.password_encryption import generate_payload
from utils.password_encryption import encrypt_password
from utils.password_encryption import compare_passwords


def test_validate_generate_payload():
    user = {'id': '123456789',
            'name': 'test test test',
            'email': 'test@gmail.com',
            'password': 'test1234'}
    payload = generate_payload(user)

    assert type(payload) is dict
    assert type(payload['exp']) is datetime.datetime
    assert payload['_id'] == user['id']
    assert payload['email'] == user['email']


def test_validate_generate_payload_without_id():
    try:
        user = {'name': 'test test test',
                'email': 'test@gmail.com',
                'password': 'test1234'}
        _ = generate_payload(user)
    except Exception as e:
        assert type(e) is KeyError


def test_validate_generate_payload_without_email():
    try:
        user = {'id': '123456789',
                'email': 'test@gmail.com',
                'password': 'test1234'}
        _ = generate_payload(user)
    except Exception as e:
        assert type(e) is KeyError


def test_encrypt_password():
    password = encrypt_password('test1234')

    assert type(password) is bytes
    assert len(password) > 1


def test_compare_password():
    password = 'test1235'
    hashed_pass = encrypt_password(password)
    pass_match = compare_passwords(password, hashed_pass.decode('utf-8'))

    assert pass_match is True


def test_compare_password_without_password():
    try:
        password = 'test1235'
        hashed_password = encrypt_password(password)
        _ = compare_passwords(password, hashed_password.decode('utf-8'))
    except Exception as e:
        assert type(e) is ValueError


def test_compare_password_without_hashed_password():
    try:
        password = 'test1235'
        hashed_password = encrypt_password(password)
        _ = compare_passwords(password, hashed_password.decode('utf-8'))
    except Exception as e:
        assert type(e) is ValueError
