from sqlalchemy.orm import Session
from app.domain.user import UserCreate
from app.infrastructure.user_repository import UserRepository

class UserService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def create_user(self, user: UserCreate):
        return self.user_repository.create_user(user)

    def get_user_by_email(self, email: str):
        return self.user_repository.get_user_by_email(email)

    def get_all_users(self):
        return self.user_repository.get_all_users()
