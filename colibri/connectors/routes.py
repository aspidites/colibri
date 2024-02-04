from fastapi_crudrouter import SQLAlchemyCRUDRouter

from .models import Connector, ConnectorSchema
from ..db import get_session

user_routes = SQLAlchemyCRUDRouter(
    db_model=Connector, 
    schema=ConnectorSchema, 
    db=get_session, 
    paginate=50,
    delete_all_route=False
)
