from uuid import uuid4

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.core.database.database import connect_with_connector
from src.core.schemas.Promotion import Promotion, PromotionCreate
from src.core.service import PromotionService

routeur = APIRouter()


@routeur.get("/", response_model=List[Promotion])
async def get_all_promotions(db: Session = Depends(connect_with_connector)):
    return PromotionService.get_all_promotions(db)


@routeur.post("/")
async def create_promotion(promotion: PromotionCreate, db: Session = Depends(connect_with_connector)):
    unique_id = str(uuid4())
    complete_promotion = {"promotion_id": unique_id, "pourcentage": promotion.pourcentage,
                          "date_debut": promotion.date_debut, "date_fin": promotion.date_fin,
                          "product_id": promotion.product_id}
    return PromotionService.create_promotion(complete_promotion, db)


@routeur.get("/active_promotions/{product_id}")
async def get_active_promotions(product_id: int, db: Session = Depends(connect_with_connector)):
    return PromotionService.get_active_promotions(product_id, db)
