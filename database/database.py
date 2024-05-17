from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# aiomysql is the driver for accessing the mysql database
DATABASE_URL = "mysql+aiomysql://root:@localhost/testing"

# create_async_engine() creates an asynchronous engine instance which is helpfull to interact with the database.
engine = create_async_engine(DATABASE_URL, echo=True)

# SessionLocal: This is a factory for creating new database sessions. It's configured to use the async engine (bind=engine) and to create async sessions (class_=AsyncSession). Other configurations like autocommit, autoflush, and expire_on_commit are set as well.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
Base = declarative_base()
