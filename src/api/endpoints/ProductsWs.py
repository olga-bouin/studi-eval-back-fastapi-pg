from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.core.database.database import connect_with_connector
from src.core.schemas.Product import Product
from src.core.service import ProductService

routeur = APIRouter()


@routeur.get("/", response_model=List[Product])
async def get_all_catalogs(db: Session = Depends(connect_with_connector)):
    return ProductService.get_all_products(db)

#TODO: add a post method to create a product
@routeur.post("/")
async def create_product(product: Product):
    return ProductService.create_catalog(product)
