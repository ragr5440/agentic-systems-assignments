from db import engine
from tables import students
from sqlalchemy import insert, select

def create_student(name: str, age: int, city: str):
    with engine.begin() as connection:
        insert_query = insert(students).values(name=name, age=age, city=city)
        connection.execute(insert_query)

create_student("Alice", 20, "New York")
create_student("Rohit", 22, "Mumbai")
create_student("Rahul", 19, "Los Angeles")

