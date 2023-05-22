from pydantic import BaseModel, validator, Field
from pydantic.class_validators import Optional


class ProductBase(BaseModel):
    product_id: int = Field(..., description="ID du produit", example=1)
    libelle: str = Field(..., description="Libellé du produit", example="Caisson cuisine")
    description: str = Field(..., description="Description du produit", example="Caisson de cuisine 80cm")
    prix: float = Field(..., description="Prix du produit en euros", example=15.0)
    promotion: Optional[float] = Field(...,
                                       description="Prix promotionnel du produit en euros, en pourcentage fait entre 25% "
                                                   "et 99% du prix", example=10.0)
    image: Optional[str] = Field(..., description="URL de l'image du produit",
                                 example="https://www.ikea.com/fr/fr/images"
                                         "/products/maximera-tiroir-bas-avec"
                                         "-facade-blanc__0713361_pe729558_s5.jpg"
                                         "?f=xl")
    catalog_id: int = Field(..., description="ID du catalogue", example=8936299)


class PromoBase(BaseModel):
    promotion: float = Field(..., description="Prix promotionnel du produit en euros, en pourcentage fait entre 25% "
                                              "et 99% du prix", example=10.0)


class Product(ProductBase):

    @validator("product_id", pre=True)
    def product_id_is_primary_key(cls, value):
        return value

    @validator("catalog_id", pre=True)
    def catalog_id_is_foreign_key(cls, value):
        return value

    class Config:
        orm_mode = True


class Promo(PromoBase):

    @validator("promotion", pre=True)
    def promotion_is_between_1_and_75_percent(cls, value):
        if value < 1 or value > 75:
            raise ValueError("Pourcentage de remise doit être entre 1% et 75%")
        return value

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    libelle: str = Field(..., description="Libellé du produit", example="Caisson cuisine")
    prix: float = Field(..., description="Prix du produit en euros", example=15.0)
    image: Optional[str] = Field(..., description="URL de l'image du produit",
                                 example="https://www.ikea.com/fr/fr/images"
                                         "/products/maximera-tiroir-bas-avec"
                                         "-facade-blanc__0713361_pe729558_s5.jpg")
    catalog_id: int = Field(..., description="ID du catalogue", example=8936299)
