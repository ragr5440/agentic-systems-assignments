from fastapi import FastAPI, Request, logger
import logging
from fastapi.responses import JSONResponse


app = FastAPI()

logger = logging.getLogger("uvicorn.error")

@app.get("/hello")
def say_hello():
    return {"message": "Hello, Welcome to FastAPI!"}

@app.middleware("http")
async def process_request(request: Request, call_next):
    print("Message before processing the request")
    logger.info("Incoming request: %s %s", request.method, request.url.path)
    response = await call_next(request)
    print("Message after processing the request")
    return response

@app.exception_handler(404)
async def undefined_route(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content={"message": "The requested resource was not found."}
    )