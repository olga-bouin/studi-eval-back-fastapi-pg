from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.core.database.database import connect_with_connector
from src.core.schemas.Product import Product, Promo
from src.core.service import ProductService

routeur = APIRouter()


@routeur.get("/", response_model=List[Product])
async def get_all_products(db: Session = Depends(connect_with_connector)):
    return ProductService.get_all_products(db)


@routeur.get("/price/{product_id}", response_model=float)
async def get_price(product_id: int, db: Session = Depends(connect_with_connector)):
    return ProductService.get_price(product_id, db)


@routeur.patch("/promotion/{product_id}", response_model=float)
async def update_promotion(promo: Promo, product_id: int, db: Session = Depends(connect_with_connector)):
    return ProductService.update_promotion(promo.promotion, product_id, db)


@routeur.patch("/compute_promotion/{product_id}", tags=["compute_promotion"], response_model=float)
async def compute_promotion(product_id: int, db: Session = Depends(connect_with_connector)):
    return ProductService.compute_promotion(product_id, db)
