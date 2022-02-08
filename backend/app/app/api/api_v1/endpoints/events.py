from typing import Any, List, Optional

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()

# @router.get("/events", response_model=List[schemas.Events])
# def read_all_events(
#     db: Session = Depends(deps.get_db),
#     skip: int = 0,
#     limit: int = 100,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Retrieve all events.
#     """
#     events = crud.events.get_multi(db, skip=skip, limit=limit)
#     return events

@router.get("/", response_model=List[schemas.Events])
def read_events(
    db: Session = Depends(deps.get_db),
    lat: Optional[float] = None,
    long: Optional[float] = None,
    distance: Optional[int] = None,
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    If all three optional query parameters are passed (latitude, longitude and distance in miles),
    retrieve first event within closest distance passed between the user and all the events.
    Else retrieve all the events paginated.
    """
    if lat and long and distance:
        events = crud.events.get_by_lat_long(db, lat=lat, long=long, distance=distance, skip=skip, limit=limit)
    else:
        events = crud.events.get_multi(db, skip=skip, limit=limit)
    return events

@router.get("/eventcategorylevel1", response_model=List[schemas.EventCategoriesLevel1])
def read_event_category_level1(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve event category level 1.
    """
    eventcategorylevel1 = crud.eventcategorylevel1.get_multi(db, skip=skip, limit=limit)
    return eventcategorylevel1

@router.get("/eventcategorylevel2/{eventcategorylevel1_id}", response_model=List[schemas.EventCategoriesLevel2])
def filter_event_category_level2_by_category_level1(
    eventcategorylevel1_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve event category level 2 details by passing category level 1 id
    """
    # eventcategorylevel2 = crud.eventcategorylevel2.get_multi(db, skip=skip, limit=limit)
    eventcategorylevel2 = crud.eventcategorylevel2.get_by_category_level1(db, category_level1_id=eventcategorylevel1_id,
                                                                          skip=skip, limit=limit)
    return eventcategorylevel2


@router.get("/{event_id}", response_model=schemas.EventAttactions)
def read_attractions(
    event_id: int,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Read Attractions
    """
    attraction = crud.attraction.get_multi(db, skip=skip, limit=limit)
    return attraction
