from fastapi import FastAPI
from .web import explorer

app = FastAPI()

app.include_router(explorer.router)
