import datetime
import bcrypt


def encrypt_password(password):
    return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())


def compare_passwords(password, hashed_password):
    if bcrypt.checkpw(
        password.encode('utf8'),
        hashed_password.encode('utf-8')
      ):
        return True
    else:
        return False


def generate_payload(user):
    return {'email': user['email'],
            '_id': str(user['id']),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}
