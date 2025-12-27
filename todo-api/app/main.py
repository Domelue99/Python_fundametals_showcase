from fastapi import FastAPI
from app.routes import router


app = FastAPI(title="ToDo API")
app.include_router(router)


