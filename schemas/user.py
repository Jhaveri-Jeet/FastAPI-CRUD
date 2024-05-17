from pydantic import BaseModel


class UserModel(BaseModel):
    email: str
    hashPassword: str

    class Config:
        orm_mode = True


class UserUpdateModel(BaseModel):
    id: int
    email: str
    hashPassword: str
