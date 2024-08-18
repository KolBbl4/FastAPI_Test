from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_HOST = "localhost"
DR_PORT = 5432
DB_USER = "postgres"
DB_PASS = "postgres"
DB_NAME = "test"

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DR_PORT}/{DB_NAME}"