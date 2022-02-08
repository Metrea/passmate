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
    from .rating import Ratings


class Events_Event(Base):
    id = Column(Integer, primary_key=True, index=True)
    city_code = Column(String, nullable=True)
    city_desc = Column(String, nullable=True)
    classes = Column(JSONB, nullable=True)
    country_code = Column(String, nullable=False, index=True)
    country_desc = Column(String, nullable=True)
    event_desc = Column(String, nullable=True)
    event_info = Column(String, nullable=True)
    event_status = Column(String, nullable=False, default='live')
    event_type = Column(String, nullable=False)
    geo_data = Column(JSONB, nullable=True)
    has_no_perfs = Column(Boolean, default=False)
    is_add_on = Column(Boolean, default=False)
    is_auto_quantity_add_on = Column(Boolean, default=False)
    is_date_matched_add_on = Column(Boolean, default=False)
    is_seated = Column(Boolean, default=False)
    is_time_matched_add_on = Column(Boolean, default=False)
    need_departure_date = Column(Boolean, default=False)
    need_duration = Column(Boolean, default=False)
    need_performance = Column(Boolean, default=False)
    show_perf_time = Column(Boolean, default=False)
    category_level1_id =Column(Integer, ForeignKey("events_category_level1.id"), index=True)
    category_level2_id = Column(Integer, ForeignKey("events_category_level2.id"), index=True)
    created_at = Column(DateTime(timezone=True), server_default=utcnow())
    updated_at = Column(DateTime(timezone=True), onupdate=utcnow())
    children = relationship("Events_Attractions", cascade="all, delete",  passive_deletes=True, back_populates="parent")

class Events_Category_Level1(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=utcnow())
    updated_at = Column(DateTime(timezone=True), onupdate=utcnow())
    children = relationship("Events_Category_Level2", cascade="all, delete", passive_deletes=True, back_populates="parent")

class Events_Category_Level2(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    category_level1_id = Column(Integer, ForeignKey("events_category_level1.id", ondelete="CASCADE"))
    created_at = Column(DateTime(timezone=True), server_default=utcnow())
    updated_at = Column(DateTime(timezone=True), onupdate=utcnow())
    parent = relationship("Events_Category_Level1", back_populates="children")

class Events_Attractions(Base):
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events_event.id", ondelete="CASCADE"))
    name = Column(String, default=False)
    description = Column(String, default=False)
    map_id = Column(String, default=False)
    map_category = Column(String, default=False)
    geo_data = Column(JSONB, nullable=True)
    recommended_activity_ind = Column(Boolean, default=False)
    queue_time_display = Column(String, default=False)
    virtual_queue_ind = Column(Boolean, default=False)
    paid_skip_the_line = Column(String, default=False)
    special_operating_time_ind = Column(Boolean, default=False)
    show_duration = Column(String, default=False)
    opening_time = Column(String, default=False)
    closing_time = Column(String, default=False)
    spot_times = Column(String, default=False)
    food_ordering_ind = Column(Boolean, default=False)
    food_menu = Column(String, default=False)
    activity_rating = Column(Integer, default=False)
    target_market = Column(String, default=False)
    height_requirement = Column(Integer, default=False)
    picture = Column(String, default=False)
    parent = relationship("Events_Event", back_populates="children")