from db import engine
from sqlalchemy import Table, Column, Integer, String, CheckConstraint, MetaData

metadata = MetaData()

students = Table(
    "students", metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("age", Integer, CheckConstraint("age > 18")),
    Column("city", String)
)

def create_tables():
    metadata.create_all(engine)

