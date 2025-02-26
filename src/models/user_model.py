from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from passlib.context import CryptContext
import re
from pydantic import BaseModel, EmailStr

Base = declarative_base()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "tbl_users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    created_date = Column(DateTime, index=True, default=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    is_deleted = Column(Boolean, index=True, default=True)
    updated_date = Column(DateTime, nullable=True)

    @staticmethod
    def hash_password(password: str) -> str:
        """Hash password menggunakan bcrypt"""
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verifikasi password yang dimasukkan dengan yang tersimpan"""
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validasi format email menggunakan regex"""
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None
