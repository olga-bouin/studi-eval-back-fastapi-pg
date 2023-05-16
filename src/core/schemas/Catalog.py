from pydantic import BaseModel, validator, Field


class CatalogBase(BaseModel):
    catalog_id: int = Field(..., description="ID du catalogue", example=8936299)
    libelle: str = Field(..., description="Libellé du catalogue", example="Cuisine")


class Catalog(CatalogBase):

    @validator("catalog_id", pre=True)
    def catalog_id_is_primary_key(cls, value):
        return value

    class Config:
        orm_mode = True
