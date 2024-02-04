from fastapi_crudrouter import SQLAlchemyCRUDRouter

from .models import Company, CompanySchema
from ..db import get_session

user_routes = SQLAlchemyCRUDRouter(
    db_model=Company, 
    schema=CompanySchema, 
    db=get_session, 
    paginate=50,
    delete_all_route=False
)
