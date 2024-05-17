from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import SessionLocal
from controllers.userController import *
from schemas.user import *
from database.database import SessionLocal

router = APIRouter()
def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def root():
    return {"message": "Hello, World!"}


@router.get("/users/{userId}", response_model=UserModel)
async def getAllUser(userId: int, db: AsyncSession = Depends(getDb)):
    user = await getUser(db, userId)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users", response_model=list[UserModel])
async def get_all_users_endpoint(db: AsyncSession = Depends(getDb)):
    users = await getAllUsers(db)
    return users


@router.post("/user/add", response_model=UserModel)
async def addUser(user: UserModel, db: AsyncSession = Depends(getDb)):
    createdUser = await createUser(db, user)
    return createdUser


@router.put("/user/update", response_model=UserModel)
async def modifyUser(user: UserUpdateModel, db: AsyncSession = Depends(getDb)):
    modifyUser = await updateUser(user, db)
    return modifyUser


@router.delete("/user/delete/{userId}")
async def removeUser(userId: int, db: AsyncSession = Depends(getDb)):
    user = await deleteUser(userId, db)
    return user
