from typing import Any, Dict, Optional, Union, List

from geopy.distance import great_circle
from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase
#Import the table models needed here
from app.models.events import Events_Event, Events_Category_Level1, Events_Category_Level2, Events_Attractions
from app.schemas.events import EventsCreate, EventsUpdate, EventCategoryLevel1Create, EventCategoryLevel1Update, EventCategoryLevel2Create, EventCategoryLevel2Update, EventAttractionsCreate, EventAttractionsUpdate

# will need to add in price and rating (system is not built) to filtering options
class CRUDEvent(CRUDBase[Events_Event, EventsCreate, EventsUpdate]):
    def get_by_lat_long(
        self, db: Session, *, lat: float, long: float, distance: int, skip: int = 0, limit: int = 100
    ) -> List[Events_Event]:
        results = db.query(self.model).enable_eagerloads(False).all()
        for result in results:
            p1 = (result.geo_data["latitude"], result.geo_data["longitude"])
            p2 = (lat, long)
            haversine_distance = great_circle(p1, p2).miles
            print(result.geo_data, p1, p2, haversine_distance)
            if haversine_distance <= distance:
                print('Event id:{} matched the distance criteria.'.format(result.event_id))
                yield(result)
        return(None)

class CRUDEventCategoryLevel1(CRUDBase[Events_Category_Level1, EventCategoryLevel1Create, EventCategoryLevel1Update]):
    pass
    # def is_active(self, user: User) -> bool:
    #     return user.is_active
    #
    # def is_superuser(self, user: User) -> bool:
    #     return user.is_superuser

class CRUDEventCategoryLevel2(CRUDBase[Events_Category_Level2, EventCategoryLevel2Create, EventCategoryLevel2Update]):
    def get_by_category_level1(
        self, db: Session, *, category_level1_id: int, skip: int = 0, limit: int = 100
    ) -> List[Events_Category_Level2]:
        return (
            db.query(self.model)
            .filter(Events_Category_Level2.category_level1_id == category_level1_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

class CRUDEventAttraction(CRUDBase[Events_Attractions, EventAttractionsCreate, EventAttractionsUpdate]):
    pass
    # def is_active(self, user: User) -> bool:
    #     return user.is_active
    #
    # def is_superuser(self, user: User) -> bool:
    #     return user.is_superuser

events = CRUDEvent(Events_Event)
eventcategorylevel1 = CRUDEventCategoryLevel1(Events_Category_Level1)
eventcategorylevel2 = CRUDEventCategoryLevel2(Events_Category_Level2)
eventattractions = CRUDEventAttraction(Events_Attractions)
