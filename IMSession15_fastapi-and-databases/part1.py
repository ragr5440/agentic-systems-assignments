from fastapi import FastAPI, Query, Path, HTTPException
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, CheckConstraint, insert, select
import json
import dbops

from db import engine
from tables import students, create_tables

app = FastAPI()

create_tables()

@app.get("/hello")
def say_hello():
    return {"message": "Hello, World!"}

@app.get("/students")
def get_all_students():
    with engine.connect() as conn:
        result = conn.execute(select(students)).mappings().all()
    return [dict(row) for row in result]


@app.get("/rahulcitychange")
def change_rahul_city(newcity: str = Query(..., description="Enter the new city for Rahul")):
    with engine.begin() as conn:
        update_query = students.update().where(students.c.name == "Rahul").values(city=newcity)
        result = conn.execute(update_query)
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Student named Rahul not found")    
    return {"message": "City updated successfully"}

@app.get("/ageenforce")
def enforce_age():
    with engine.begin() as conn:
        delete_query = students.delete().where(students.c.age <= 20)
        result = conn.execute(delete_query)
    return {"message": f"Students aged 20 or younger have been removed from the database"}
