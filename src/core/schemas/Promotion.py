from pydantic import BaseModel, validator
from datetime import datetime as DateTime


class PromotionBase(BaseModel):
    promotion_id: int = None
    pourcentage: float
    date_debut: DateTime
    date_fin: DateTime
    product_id: int


class Promotion(PromotionBase):

    @validator("promotion_id", pre=True)
    def product_id_is_primary_key(cls, value):
        return value

    @validator("product_id", pre=True)
    def catalog_id_is_foreign_key(cls, value):
        return value

    class Config:
        orm_mode = True
