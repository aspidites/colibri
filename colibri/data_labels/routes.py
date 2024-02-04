from fastapi_crudrouter import SQLAlchemyCRUDRouter

from .models import DataLabel, DataLabelSchema
from ..db import get_session

user_routes = SQLAlchemyCRUDRouter(
    db_model=DataLabel, 
    schema=DataLabelSchema, 
    db=get_session, 
    paginate=50,
    delete_all_route=False
)
