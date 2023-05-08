from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.core.database.database import connect_with_connector
from src.core.schemas.Catalog import Catalog
from src.core.service import CatalogService

routeur = APIRouter()


@routeur.get("/", response_model=List[Catalog])
async def get_all_catalogs(db: Session = Depends(connect_with_connector)):
    return CatalogService.get_all_catalogs(db)

#TODO: add a post method to create a catalog
@routeur.post("/")
async def create_catalog(catalog: Catalog):
    return CatalogService.create_catalog(catalog)
