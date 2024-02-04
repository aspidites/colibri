from sqlmodel import SQLModel, Field

class DataAssetSchema(SQLModel):
    pass


class DataAsset(DataAssetSchema, table=True):
    __tablename__ = "data_assets"

    id: int = Field(primary_key=True)


