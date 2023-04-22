from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

#from src.core.database.database import connect_with_connector
from src.core.schemas.Catalog import Catalog
from src.core.service import CatalogService

routeur = APIRouter()


@routeur.get("/", response_model=List[Catalog])
# @routeur.get("/")
async def get_all_catalogs():
    # async def get_all_catalogs(db: Session = Depends(connect_with_connector)):
    # return CatalogService.get_all_catalogs(db)
    return CatalogService.get_all_catalogs()


@routeur.post("/")
async def create_catalog(catalog: Catalog):
    return CatalogService.create_catalog(catalog)
