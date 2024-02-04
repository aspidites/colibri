from sqlmodel import SQLModel, Field

class DataLabelSchema(SQLModel):
    pass


class DataLabel(DataLabelSchema, table=True):
    __tablename__ = "data_labels"

    id: int = Field(primary_key=True)

