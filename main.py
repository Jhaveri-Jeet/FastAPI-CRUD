from fastapi import FastAPI
from controllers.userController import *
from database.database import engine, Base
import contextlib
from routes.userRoutes import router as userRoutes


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(userRoutes)
