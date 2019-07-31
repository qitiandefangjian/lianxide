from flask import dbort
from flask_login import current_user
from functools import wraps
from jobplus.models import User

def role_required(role):

    def decorator(func):

        @wraps(func)
        def wrapper(*args,**kwrargs):
            if not current_user.is_authenticated or current_user.role < role:
                abort(404)
            return func(*args,**kwrargs)
        return wrapper
    return decorator

euser_requeired = role_required(User.EUSER_ROLE)
user_requeired = role_required(User.USER_ROLE)
admin_requeired = role_required(User.ADMIN_ROLE)

