import time

def get_user_registration_data():
    return {
        "email": f"user_{int(time.time())}@mail.com",
        "password": "qaz",
        "password_submit": "qaz",
    }
