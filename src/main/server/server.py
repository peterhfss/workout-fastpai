from fastapi import FastAPI
from src.main.routes.athletes_routes import athletes_routes

app = FastAPI()

app.include_router(athletes_routes)
