from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import UserModel, UserUpdateModel
from models.models import User
from sqlalchemy.future import select
from fastapi import HTTPException


async def createUser(db: AsyncSession, user: UserModel):
    newUser = User(email=user.email, hashPassword=user.hashPassword)
    if newUser is None:
        raise HTTPException(status_code=400, detail="User not created")

    db.add(newUser)
    await db.commit()
    await db.refresh(newUser)
    return newUser


async def getUser(db: AsyncSession, userId: int):
    result = await db.execute(select(User).filter(User.id == userId))
    return result.scalars().first()


async def getAllUsers(db: AsyncSession) -> list[UserModel]:
    result = await db.execute(select(User))
    return result.scalars().all()


async def updateUser(user: UserUpdateModel, db: AsyncSession):
    result = await db.execute(select(User).filter(User.id == user.id))
    updateUser = result.scalars().first()
    if updateUser is None:
        raise HTTPException(status_code=404, detail="User not found")

    updateUser.email = user.email
    updateUser.hashPassword = user.hashPassword
    await db.commit()
    await db.refresh(updateUser)
    return updateUser


async def deleteUser(userId: int, db: AsyncSession):
    result = await db.execute(select(User).filter(User.id == userId))
    deleteUser = result.scalars().first()
    if deleteUser is None:
        raise HTTPException(status_code=404, detail="User not found")

    await db.delete(deleteUser)
    await db.commit()
    raise HTTPException(status_code=200, detail="User deleted")
