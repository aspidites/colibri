from sqlmodel import SQLModel, Field


class UserSchema(SQLModel):
    email: str


class UserCreateSchema(UserSchema):
    pass


class UserUpdateSchema(UserSchema):
    pass


class User(UserSchema, table=True):
    __tablename__ = "users"
    id: int = Field(primary_key=True)
