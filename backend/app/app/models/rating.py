from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import JSON, JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression
from sqlalchemy.ext.compiler import compiles

from app.db.base_class import Base

class utcnow(expression.FunctionElement):
    type = DateTime()

@compiles(utcnow, 'postgresql')
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .events import Events_Event


class Rating(Base):
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events_event.id"), index=True)
    user_id = Column(Integer, ForeignKey("user.id"), index=True)
    body = Column(String, default=False)
    owner = relationship("User", back_populates="ratings")
    created_at = Column(DateTime(timezone=True), server_default=utcnow())
    updated_at = Column(DateTime(timezone=True), onupdate=utcnow())
    score = Column(Integer)