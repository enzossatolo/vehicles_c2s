import sys
import os

import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from src.config.config import logger

Base = declarative_base()
_async_db_engine = None

DB_DB = os.getenv('DB_DB', 'database.db')


def get_db_engine():
    conn_str = sa.engine.url.URL.create(
        drivername='sqlite',
        database=DB_DB
    )
    return create_engine(
        conn_str,
        echo=True,
        future=True
    )


def get_async_db_engine(
    pool_size: int = 5,
    pool_recycle: int = 1000,
    max_overflow: int = 10,
    pool_timeout: float = 30.0,
    async_timeout: int | float | None = 60
) -> AsyncEngine:
    global _async_db_engine
    if _async_db_engine is not None:
        return _async_db_engine

    conn_str = sa.engine.url.URL.create(
        drivername='sqlite+aiosqlite',
        database=DB_DB
    )

    try:
        _async_db_engine = create_async_engine(
            conn_str,
            pool_recycle=pool_recycle,
            pool_size=pool_size,
            max_overflow=max_overflow,
            pool_timeout=pool_timeout,
            connect_args={'timeout': async_timeout},
            future=True
        )
    except Exception as e:
        logger.error(e)
        sys.exit()

    return _async_db_engine


def async_session(expire_on_commit: bool | None = False) -> sessionmaker:
    engine = get_async_db_engine()
    return sessionmaker(
        bind=engine, class_=AsyncSession, future=True,
        expire_on_commit=expire_on_commit
    )


def get_session() -> sessionmaker:
    conn_str = sa.engine.url.URL.create(
        drivername='sqlite',
        database=DB_DB
    )
    engine = create_engine(
        conn_str,
        echo=True,
        future=True
    )
    return sessionmaker(engine)


def create_all_tables():
    engine = get_db_engine()
    Base.metadata.create_all(engine)
