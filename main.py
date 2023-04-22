from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import declarative_base

from src.api import api
from src.core.database.database import connect_with_connector

origins = ["http://localhost:4200"]

app = FastAPI(title='EvaluationOlga')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.routeur, prefix='/api')
# Base = declarative_base()
# Base.metadata.create_all(connect_with_connector())