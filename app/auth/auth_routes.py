
# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from ... import schemas, models, database
# from ..utils.hashing import hash_password, verify_password
# from .auth_handler import create_access_token
# from fastapi.security import OAuth2PasswordRequestForm

# router = APIRouter()

# @router.post("/signup", response_model=schemas.UserOut)
# def signup(user: schemas.UserCreate, db: Session = Depends(database.SessionLocal)):
#     db_user = db.query(models.User).filter(models.User.email == user.email).first()
#     if db_user:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
   
#     hashed_password = hash_password(user.password)
#     new_user = models.User(email=user.email, hashed_password=hashed_password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @router.post("/login")
# def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.SessionLocal)):
#     db_user = db.query(models.User).filter(models.User.email == form_data.username).first()
#     if not db_user or not verify_password(form_data.password, db_user.hashed_password):
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")
   
#     access_token = create_access_token(data={"sub": db_user.email})
#     return {"access_token": access_token, "token_type": "bearer"}