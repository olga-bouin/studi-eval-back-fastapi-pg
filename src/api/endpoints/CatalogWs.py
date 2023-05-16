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


@routeur.post("/", response_model=Catalog)
async def create_catalog(catalog: Catalog, db: Session = Depends(connect_with_connector)):
    return CatalogService.create_catalog(catalog, db)


@routeur.delete("/catalog/{catalog_id}", response_model=int)
async def delete_catalog(catalog_id: int, db: Session = Depends(connect_with_connector)):
    return CatalogService.delete_catalog(catalog_id, db)
