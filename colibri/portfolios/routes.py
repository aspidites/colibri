from fastapi_crudrouter import SQLAlchemyCRUDRouter

from .models import Portfolio, PortfolioSchema
from ..db import get_session

user_routes = SQLAlchemyCRUDRouter(
    db_model=Portfolio, 
    schema=PortfolioSchema, 
    db=get_session, 
    paginate=50,
    delete_all_route=False
)
