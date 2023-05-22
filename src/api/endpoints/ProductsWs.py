from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from core.schemas.Product import ProductCreate
from src.core.database.database import connect_with_connector
from src.core.schemas.Product import Product, Promo
from src.core.service import ProductService

routeur = APIRouter()


@routeur.get("/", response_model=List[Product])
async def get_all_products(db: Session = Depends(connect_with_connector)):
    return ProductService.get_all_products(db)


@routeur.post("/")
async def create_product(product: ProductCreate, db: Session = Depends(connect_with_connector)):
    product_id = ProductService.get_max_id(db) + 1
    complete_product = {"product_id": product_id, "libelle": product.libelle, "description": product.libelle,
                        "prix": product.prix, "promotion": product.prix, "image": product.image,
                        "catalog_id": product.catalog_id}
    return ProductService.create_product(complete_product, db)


@routeur.get("/get_max_id/", response_model=int)
async def get_max_id(db: Session = Depends(connect_with_connector)):
    return ProductService.get_max_id(db)


@routeur.get("/price/{product_id}", response_model=float)
async def get_price(product_id: int, db: Session = Depends(connect_with_connector)):
    return ProductService.get_price(product_id, db)


@routeur.patch("/promotion/{product_id}", response_model=float)
async def update_promotion(promo: Promo, product_id: int, db: Session = Depends(connect_with_connector)):
    return ProductService.update_promotion(promo.promotion, product_id, db)


@routeur.patch("/compute_promotions/{product_id}", tags=["compute_promotion"], response_model=float)
async def compute_promotion(product_id: int, db: Session = Depends(connect_with_connector)):
    return ProductService.compute_promotion(product_id, db)


@routeur.patch("/compute_promotions/")
async def compute_all_promotions(db: Session = Depends(connect_with_connector)):
    return ProductService.compute_all_promotions(db)
