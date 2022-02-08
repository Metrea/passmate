# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.item import Item  # noqa
from app.models.user import User  # noqa
from app.models.events import Events_Event, Events_Category_Level1, Events_Category_Level2
from app.models.events import Events_Attractions
from app.models.rating import Rating # noqa