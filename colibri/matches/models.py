from sqlmodel import SQLModel, Field

class MatchSchema(SQLModel):
    pass


class Match(MatchSchema, table=True):
    __tablename__ = "matches"

    id: int = Field(primary_key=True)


