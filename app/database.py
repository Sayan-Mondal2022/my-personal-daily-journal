import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

load_dotenv()

# For local DB setup MySQL
# USER_NAME = os.getenv("USER_NAME")
# PASSWORD = os.getenv("PASSWORD")
# DATABASE_NAME = os.getenv("DATABASE_NAME")
# DATABASE_URL = f"mysql+pymysql://{USER_NAME}:{PASSWORD}@localhost/{DATABASE_NAME}"

# For Deployment
DATABASE_URL = os.getenv("POSTGRESQL_CONNECTION")


# DEBUGGING STATEMENT TO TEST THE URL
# print(DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ASYNCHRONOUS
# DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
# engine = create_async_engine(DATABASE_URL, echo=True)
# AsyncSessionLocal = sessionmaker(
#     bind=engine, class_=AsyncSession, expire_on_commit=False
# )

Base = declarative_base()
