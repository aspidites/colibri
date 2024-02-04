from fastapi_crudrouter import SQLAlchemyCRUDRouter

from .models import User, UserSchema, UserCreateSchema, UserUpdateSchema
from ..db import get_session

user_routes = SQLAlchemyCRUDRouter(
    db_model=User, 
    schema=UserSchema, 
    create_schema=UserCreateSchema, 
    update_schema=UserUpdateSchema,
    db=get_session, 
    paginate=50,
    delete_all_route=False
)
