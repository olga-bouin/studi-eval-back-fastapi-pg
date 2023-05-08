from fastapi import APIRouter

from src.api.endpoints import ProductsWs, CatalogWs

routeur = APIRouter()

routeur.include_router(ProductsWs.routeur, prefix='/products',
                       tags=["products"],
                       responses={404: {"description": "Impossible"}})

routeur.include_router(CatalogWs.routeur, prefix='/catalog',
                       tags=["catalog"],
                       responses={404: {"description": "Impossible"}})
