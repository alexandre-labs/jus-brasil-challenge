from fastapi import FastAPI

from .api import health
from .api import query

app = FastAPI()

app.include_router(health.router)
app.include_router(query.router)
