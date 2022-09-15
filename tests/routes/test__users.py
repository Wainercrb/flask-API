from flask import url_for

from model.user import User

def test_create_user(app_with_db):
    response = app_with_db.post(url_for("user_route.login"),
                                json={
                                    "password": "Abcdefgh",
                                    "email": "john@mail.com",
                                })

    assert response.status_code == 403
    # count = db.session.execute(select(func.count(User.id)).where(User.username == "John")).scalar_one()
    # assert count == 1