from sqlmodel import SQLModel, Field


class ReportSchema(SQLModel):
    pass


class Report(ReportSchema, table=True):
    __tablename__ = "reports"

    id: int = Field(primary_key=True)
