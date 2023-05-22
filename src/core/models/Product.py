from sqlalchemy import Integer, Column, String, Numeric


class Product:
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True)
    libelle = Column(String)
    description = Column(String)
    prix = Column(Numeric)
    promotion = Column(Numeric)
    image = Column(String)
    catalog_id = Column(Integer)
