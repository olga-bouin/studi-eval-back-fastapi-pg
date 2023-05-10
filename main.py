import os
from dotenv import load_dotenv
from pathlib import Path
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.api import api


def add_middleware(app):
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    origins = ["http://localhost:4200", "http://localhost:8080", os.getenv("FRONTEND_URL")]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def include_router(app):
    app.include_router(api.routeur, prefix='/api')


def start_application():
    app: FastAPI = FastAPI(title='EvaluationOlga')
    add_middleware(app)
    include_router(app)
    return app


app = start_application()
