from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database import get_db, init_db
from app.application.user_service import UserService
from app.domain.user import UserCreate, UserResponse

app = FastAPI()

init_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to the DDD DevOps Microservice!"}

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    db_user = user_service.get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(user)

@app.get("/users/", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.get_all_users()
