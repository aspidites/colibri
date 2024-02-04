from fastapi_crudrouter import SQLAlchemyCRUDRouter

from .models import Match, MatchSchema
from ..db import get_session

user_routes = SQLAlchemyCRUDRouter(
    db_model=Match, 
    schema=MatchSchema, 
    db=get_session, 
    paginate=50,
    delete_all_route=False
)
