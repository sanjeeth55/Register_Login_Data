import jwt
from django.conf import settings
from datetime import datetime, timezone

def generate_jwt(employee):
    payload = {
        "employee_id": employee.id,
        "username": employee.user_name,
        "exp": datetime.now(tz=timezone.utc) + settings.JWT_EXPIRATION_DELTA,
        "iat": datetime.now(tz=timezone.utc),
    }

    token = jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )

    return token
