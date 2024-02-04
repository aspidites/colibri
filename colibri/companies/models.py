from sqlmodel import SQLModel, Field


class CompanySchema(SQLModel):
    pass


class Company(CompanySchema, table=True):
    __tablename__ = "matches"

    id: int = Field(primary_key=True)

