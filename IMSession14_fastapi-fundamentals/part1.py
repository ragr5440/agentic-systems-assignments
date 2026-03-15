#py -m pip install fastapi pydantic uvicorn => to install the required package

from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/search")
    
def search(name: Optional[str] = None, age: Optional[int] = None):
    return {"name": name, "age": age}
