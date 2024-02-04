from sqlmodel import SQLModel, Field

class FileSchema(SQLModel):
    pass


class File(FileSchema, table=True):
    __tablename__ = "files"

    id: int = Field(primary_key=True)

