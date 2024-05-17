from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    hashPassword = Column(String(255))

    details = relationship("UserDetails", back_populates="user")


class UserDetails(Base):
    __tablename__ = "UserDetails"

    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey("Users.id"))
    address = Column(String(255))

    user = relationship("User", back_populates="details")
