from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.core.database.database import connect_with_connector
from src.core.schemas.Promotion import Promotion
from src.core.service import PromotionService

routeur = APIRouter()


@routeur.get("/", response_model=List[Promotion])
async def get_all_promotions(db: Session = Depends(connect_with_connector)):
    return PromotionService.get_all_promotions(db)


@routeur.post("/")
async def create_product(promotion: Promotion, db: Session = Depends(connect_with_connector)):
    return PromotionService.create_promotion(promotion, db)
