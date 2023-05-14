from fastapi import APIRouter

from src.api.endpoints import ProductsWs, CatalogWs, PromotionsWs

routeur = APIRouter()

routeur.include_router(ProductsWs.routeur, prefix='/products',
                       tags=["products"],
                       responses={404: {"description": "Impossible"}})

routeur.include_router(CatalogWs.routeur, prefix='/catalog',
                       tags=["catalog"],
                       responses={404: {"description": "Impossible"}})

routeur.include_router(PromotionsWs.routeur, prefix='/promotions',
                       tags=["promotions"],
                       responses={404: {"description": "Impossible"}})