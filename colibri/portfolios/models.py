from sqlmodel import SQLModel, Field

class PortfolioSchema(SQLModel):
    pass


class Portfolio(PortfolioSchema, table=True):
    __tablename__ = "portfolios"

    id: int = Field(primary_key=True)


