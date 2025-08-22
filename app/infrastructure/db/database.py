"""Database connection management for SQLModel in FastAPI."""

from app.config import settings
from sqlmodel import Session, create_engine


_engine = None

def get_engine():
    """Returns a singleton SQLModel engine instance.

    Returns:
        Engine: A SQLModel engine instance connected to the configured database.
    """
    global _engine
    if _engine is None:
        _engine = create_engine(
            settings.database_url,
            pool_size=10,
            max_overflow=20,
            pool_timeout=30,
            pool_recycle=1800,
        )
    return _engine


def get_session():
    """Dependency generator for database session.

    Yields a session for use in FastAPI routes and closes it after use.
    """
    with Session(get_engine()) as session:
        yield session
