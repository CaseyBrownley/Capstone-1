
# import jwt
# from datetime import datetime, timedelta
# from app.config import JWT_SECRET_KEY

# def create_access_token(data: dict):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=30)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm="HS256")
#     return encoded_jwt

# def verify_access_token(token: str):
#     try:
#         payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
#         return payload if "sub" in payload else None
#     except jwt.ExpiredSignatureError:
#         return None