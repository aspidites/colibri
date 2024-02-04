from fastapi_crudrouter import SQLAlchemyCRUDRouter

from .models import CapitalApplication, CapitalApplicationSchema
from ..db import get_session

user_routes = SQLAlchemyCRUDRouter(
    db_model=CapitalApplication, 
    schema=CapitalApplicationSchema, 
    db=get_session, 
    paginate=50,
    delete_all_route=False
)
