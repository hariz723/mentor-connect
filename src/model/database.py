from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine # type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base # type: ignore


# local imports 
from config import settings


engine = create_async_engine(settings.database_url, echo=True, future=True)
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)
Base = declarative_base()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
    