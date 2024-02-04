from sqlmodel import SQLModel, Field

class ConnectorSchema(SQLModel):
    pass


class Connector(ConnectorSchema, table=True):
    __tablename__ = "connectors"

    id: int = Field(primary_key=True)


