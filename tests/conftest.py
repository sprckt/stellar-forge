import pytest
from sqlmodel import Field, SQLModel


@pytest.fixture
def user_class():
    class TestUser(SQLModel, table=True, ):
        id: int = Field(default=None, primary_key=True)
        name: str
        age: int

    return TestUser()
