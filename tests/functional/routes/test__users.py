from flask import url_for


def test_create_user(app_with_db):
    response = app_with_db.post(url_for('user_route.signup'),
                                json={
                                    'mobile': '+ 506 432132',
                                    'password': 'test1234',
                                    'email': 'test@test.com',
                                    'name': 'Test Test Test',
                                    'image': 'img-tes.png'
                                })

    assert response.status_code == 200


def test_create_user_same_credentials(app_with_db):
    response = app_with_db.post(url_for('user_route.signup'),
                                json={
                                    'mobile': '+ 506 432132',
                                    'password': 'test1234',
                                    'email': 'test@test.com',
                                    'name': 'Test Test Test',
                                    'image': 'img-tes.png'
                                })

    assert response.status_code == 404


def test_login(app_with_db):
    response = app_with_db.post(url_for('user_route.login'),
                                json={
                                    'password': 'test1234',
                                    'email': 'test@test.com',
                                })

    assert response.status_code == 200


def test_login_invalid_password(app_with_db):
    response = app_with_db.post(url_for('user_route.login'),
                                json={
                                    'password': 'test12345',
                                    'email': 'test@test.com',
                                })

    assert response.status_code == 403
