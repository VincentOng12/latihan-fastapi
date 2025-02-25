from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.config.app_config import settings

# Buat engine database dengan asyncpg
engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)

# Buat session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Dependency untuk mendapatkan sesi database
async def get_db():
    async with SessionLocal() as session:
        yield session
