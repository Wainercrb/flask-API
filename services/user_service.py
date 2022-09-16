import os
import json
from flask import make_response, jsonify
from model.user import User
from utils.JwtToken import generate_token
from utils.passwordEncryption import encrypt_password
from utils.passwordEncryption import compare_passwords
from utils.passwordEncryption import generate_payload


def signup_service(userdata):
    try:
        email_check = User.objects[:1](email=userdata['email'])

        if email_check:
            return make_response({'message': 'email already exists'}, 404)

        name = userdata['name']
        email = userdata['email']
        image = userdata['image']
        mobile = userdata['mobile']
        password = encrypt_password(userdata['password'])

        user = User(name=name,
                    email=email,
                    image=image,
                    mobile=mobile,
                    password=password)

        user.save()

        return make_response({'message': 'succesfully inserted'}, 200)

    except Exception as e:
        return make_response({'message': str(e)}, 404)


def login_service(user_credentials):
    try:
        users = User.objects[:1](email=user_credentials['email'])

        if (len(users) <= 0):
            return make_response({'message': 'Invalid password'}, 403)

        secret = os.environ.get('TOKEN_SECRET')

        for user in users:
            if compare_passwords(
                  user_credentials['password'],
                  user['password']
              ):

                token = generate_token(generate_payload(user), secret)

                user['password'] = '-'

                return make_response(
                    {'token': token, 'user': json.loads(user.to_json())},
                    200
                )

            else:
                return make_response({'message': 'Invalid password'}, 403)

    except Exception as e:
        return make_response({'message': str(e)}, 404)


def get_users_service():
    try:
        users = User.objects.to_json()

        return jsonify({'users': users}), 200

    except Exception as e:
        return make_response({'message': str(e)}, 404)
