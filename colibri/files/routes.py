from fastapi_crudrouter import SQLAlchemyCRUDRouter

from .models import File, FileSchema
from ..db import get_session

user_routes = SQLAlchemyCRUDRouter(
    db_model=File, 
    schema=FileSchema, 
    db=get_session, 
    paginate=50,
    delete_all_route=False
)
