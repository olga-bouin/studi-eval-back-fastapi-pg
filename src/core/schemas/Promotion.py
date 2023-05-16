from pydantic import BaseModel, validator, Field
from datetime import datetime as DateTime


class PromotionBase(BaseModel):
    promotion_id: str = Field(..., description="ID autogénéré de la promotion", example="ca17c671-215b-48c2-8ea0-29cce67725ef")
    pourcentage: float = Field(..., description="Pourcentage de remise du produit, compris entre 1% et 75%", example=10.0)
    date_debut: DateTime = Field(..., description="Date et heure du début de la promotion", example="2023-01-01 10:00:00")
    date_fin: DateTime = Field(..., description="Date de heure de la fin de la promotion", example="2024-01-01 15:00:00")
    product_id: int = Field(..., description="ID du produit", example=1)


class PromotionCreate(BaseModel):
    pourcentage: float = Field(..., description="Pourcentage de remise du produit, compris entre 1% et 75%", example=10.0)
    date_debut: DateTime = Field(..., description="Date et heure du début de la promotion", example="2023-01-01 10:00:00")
    date_fin: DateTime = Field(..., description="Date de heure de la fin de la promotion", example="2024-01-01 15:00:00")
    product_id: int = Field(..., description="ID du produit", example=1)


class Promotion(PromotionBase):

    @validator("promotion_id", pre=True)
    def product_id_is_primary_key(cls, value):
        return value

    @validator("pourcentage", pre=True)
    def pourcentage_is_between_1_and_75(cls, value):
        if value < 1 or value > 75:
            raise ValueError("Pourcentage de remise doit être entre 1% et 75%")
        return value

    @validator("product_id", pre=True)
    def catalog_id_is_foreign_key(cls, value):
        return value

    class Config:
        orm_mode = True
