from sqlalchemy.orm import Session
from app.domain.user import User, UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: UserCreate):
        db_user = User(name=user.name, email=user.email)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def get_all_users(self):
        return self.db.query(User).all()
