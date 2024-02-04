from sqlmodel import SQLModel, Field

class CapitalApplicationSchema(SQLModel):
    pass


class CapitalApplication(CapitalApplicationSchema, table=True):
    __tablename__ = "capital_applications"

    id: int = Field(primary_key=True)



