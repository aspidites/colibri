from fastapi_crudrouter import SQLAlchemyCRUDRouter

from .models import Report, ReportSchema
from ..db import get_session

user_routes = SQLAlchemyCRUDRouter(
    db_model=Report, 
    schema=ReportSchema, 
    db=get_session, 
    paginate=50,
    delete_all_route=False
)
