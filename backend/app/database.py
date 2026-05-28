from __future__ import annotations

import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DATABASE_URL = f"sqlite:///{BASE_DIR / 'stylesnap.db'}"


class Base(DeclarativeBase):
    pass


DATABASE_URL = DEFAULT_DATABASE_URL
connect_args: dict[str, bool] = {}
engine = None
SessionLocal = None


def configure_database(database_url: str | None = None) -> None:
    global DATABASE_URL, connect_args, engine, SessionLocal

    DATABASE_URL = database_url or os.getenv("STYLESNAP_DATABASE_URL", DEFAULT_DATABASE_URL)
    connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
    engine = create_engine(DATABASE_URL, connect_args=connect_args)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


configure_database()


def initialize_database() -> None:
    if engine is None:
        configure_database()
    Base.metadata.create_all(bind=engine)


def get_database_label() -> str:
    if engine is None:
        configure_database()
    return engine.url.get_backend_name()


def get_db() -> Session:
    if SessionLocal is None:
        configure_database()

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
