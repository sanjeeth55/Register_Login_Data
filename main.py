######################################################

    # FastAPI for access token

#########################################################
# JWT - Json Web Token

# Str - Header.Payload.signature

# Header - what type algaritham

# Header = type : JWT, alg = HS256/RSA
# payloard = User data,
# Signature = encode infor

# login endpoint and secrect data
# JWT Token Creatting

# from datetime import datetime, timedelta
# from fastapi import FastAPI, HTTPException
# from jose import JWTError, jwt

# # configuration
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 120
# SECRET_KEY = "thesecretkeyforapp_9909"

# app = FastAPI()

# # create token
# def create_token(uname: str):
#     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     payload = {
#         "username": uname,
#         "exp": expire
#     }
#     return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# # verify token
# def verify_token(token: str):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload["username"]
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid or expired token")

# # login endpoint
# @app.post("/login")
# def login(uname: str, password: str):
#     if uname == "admin" and password == "123":
#         token = create_token(uname)  
#         return {"access_token": token}
#     raise HTTPException(status_code=400, detail="Invalid credentials")

# # secure endpoint
# @app.get("/secure_data")
# def sec_data(token: str):
#     uname = verify_token(token)
#     return {"message": f"Hello {uname}, Secure data from the endpoint"}


######################################################

    # Default django

#########################################################
