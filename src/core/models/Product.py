from sqlalchemy import Integer, Column, String, Numeric


class Product:
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True)
    libelle = Column(String)
    description = Column(String)
    prix = Column(Numeric)
    promotion = Column(Numeric) #TODO : nullable=True is not working, if no data in database, error
    image = Column(String, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAW4xy0lwmiEo6hcL6Ax3IX1KCQ78A70bArUo3Bsz_gUIi35VZkJEOvUMtMA&s")
    catalog_id = Column(Integer)
