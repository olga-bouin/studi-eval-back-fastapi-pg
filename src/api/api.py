from fastapi import APIRouter

from src.api.endpoints import ProductWs, CatalogWs

routeur = APIRouter()
# routeur.include_router(ProductWs.routeur, prefix='/product',
#                        tags=["product"],
#                        responses={404: {"description": "Impossible"}})

routeur.include_router(CatalogWs.routeur, prefix='/catalog',
                       tags=["catalog"],
                       responses={404: {"description": "Impossible"}})
