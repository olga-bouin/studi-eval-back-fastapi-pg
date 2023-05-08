from pydantic import BaseModel, validator


class CatalogBase(BaseModel):
    catalog_id: int = None
    libelle: str


class Catalog(CatalogBase):

    @validator("catalog_id", pre=True)
    def catalog_id_is_primary_key(cls, value):
        return value

    class Config:
        orm_mode = True
