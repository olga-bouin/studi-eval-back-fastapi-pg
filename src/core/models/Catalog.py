from sqlalchemy import Integer, Column, String


class Catalog:
    __tablename__ = "catalog"
    catalog_id = Column(Integer, primary_key=True)
    libelle = Column(String)
