from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties for Different Event Models: i.e Events_Event, Events_Category_Level1, Events_Category_Level2
class EventsBase(BaseModel):
    # id = Column(Integer, primary_key=True, index=True)
    city_code: str = None
    city_desc: str = None
    classes: dict = None
    country_code: str = None
    country_desc: str = None
    event_desc: str = None
    event_info: str = None
    event_status: str = None
    event_type: str = None
    geo_data: dict = None
    has_no_perfs: bool = None
    is_add_on: bool = None
    is_auto_quantity_add_on: bool = None
    is_date_matched_add_on: bool = None
    is_seated: bool = None
    is_time_matched_add_on: bool = None
    need_departure_date: bool = None
    need_duration: bool = None
    need_performance: bool = None
    show_perf_time: bool = None
    category_level1_id: int = None
    category_level2_id: int = None
    event_id: int = None

class EventCategoryLevel1Base(BaseModel):
    name: str = None

class EventCategoryLevel2Base(BaseModel):
    name: str = None


class EventAttractionsBase(BaseModel):
    # id = Column(Integer, primary_key=True, index=True)
    event_id: int = None
    name: str = None
    description: str = None
    map_id: str = None
    map_category: str = None
    geo_data: dict = None
    recommended_activity_ind: bool = None
    queue_time_display: str = None
    virtual_queue_ind: bool = None
    paid_skip_the_line: str = None
    special_operating_time_ind: bool = None
    show_duration: str = None
    opening_time: str = None
    closing_time: str = None
    spot_times: str = None
    food_ordering_ind: bool = None
    food_menu: str = None
    activity_rating: int = None
    target_market: str = None
    height_requirement: int = None
    picture: str = None

# Properties to receive via API on creation for Different Event Models
class EventsCreate(EventsBase):
    pass

class EventCategoryLevel1Create(EventCategoryLevel1Base):
    pass

class EventCategoryLevel2Create(EventCategoryLevel2Base):
    # name: str
    pass

class EventAttractionsCreate(EventAttractionsBase):

    pass

# Properties to receive via API on update for Different Event Models
class EventsUpdate(EventsBase):
    pass

class EventCategoryLevel1Update(EventCategoryLevel1Base):
    pass

class EventCategoryLevel2Update(EventCategoryLevel2Base):
    # password: Optional[str] = None
    pass

class EventAttractionsUpdate(EventAttractionsBase):
    pass

# Properties to retrieve from the Database via API for Different Event Models
class EventsDBBase(EventsBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class EventCategoriesLevel1DBBase(EventCategoryLevel1Base):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class EventCategoriesLevel2DBBase(EventCategoryLevel2Base):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class EventAttractionsDBBase(EventAttractionsBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

# Additional properties to return via API
class Events(EventsDBBase):
    pass

class EventCategoriesLevel1(EventCategoriesLevel1DBBase):
    pass

class EventCategoriesLevel2(EventCategoriesLevel2DBBase):
    category_level1_id: Optional[int] = None

class EventAttactions(EventAttractionsDBBase):
    event_id: Optional[int] = None