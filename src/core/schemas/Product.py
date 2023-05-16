from pydantic import BaseModel, validator


class ProductBase(BaseModel):
    product_id: int = None
    libelle: str
    description: str
    prix: float
    promotion: float
    image: str
    catalog_id: int


class Promo(BaseModel):
    promotion: float


class Product(ProductBase):

    @validator("product_id", pre=True)
    def product_id_is_primary_key(cls, value):
        return value

    @validator("catalog_id", pre=True)
    def catalog_id_is_foreign_key(cls, value):
        return value

    class Config:
        orm_mode = True
