from fastapi_crudrouter import SQLAlchemyCRUDRouter

from .models import DataAsset, DataAssetSchema
from ..db import get_session

user_routes = SQLAlchemyCRUDRouter(
    db_model=DataAsset, 
    schema=DataAssetSchema, 
    db=get_session, 
    paginate=50,
    delete_all_route=False
)
