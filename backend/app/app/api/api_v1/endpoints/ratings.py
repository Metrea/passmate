from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps


router = APIRouter()


@router.get("/", response_model=List[schemas.Rating])
def read_ratings(db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve ratings.
    """
    if crud.user.is_superuser(current_user):
        ratings = crud.rating.get_multi(db, skip=skip, limit=limit)
    else:
        ratings = crud.rating.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return ratings


@router.post("/", response_model=schemas.Rating)
def create_rating(
    *,
    db: Session = Depends(deps.get_db),
    rating_in: schemas.RatingCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new rating.
    """
    rating = crud.rating.create_with_owner(db=db, obj_in=rating_in, owner_id=current_user.id)
    return rating


@router.put("/{id}", response_model=schemas.Rating)
def update_rating(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    rating_in: schemas.RatingUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a Rating.
    """
    rating = crud.rating.get(db=db, id=id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    if not crud.user.is_superuser(current_user) and (rating.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    rating = crud.rating.update(db=db, db_obj=rating, obj_in=rating_in)
    return rating


@router.get("/{id}", response_model=schemas.Rating)
def read_rating(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get rating by ID.
    """
    rating = crud.rating.get(db=db, id=id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    if not crud.user.is_superuser(current_user) and (rating.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return rating


@router.delete("/{id}", response_model=schemas.Rating)
def delete_rating(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a rating.
    """
    rating = crud.rating.get(db=db, id=id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    if not crud.user.is_superuser(current_user) and (rating.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    rating = crud.rating.remove(db=db, id=id)
    return rating