from sqlalchemy import Integer, Column, Numeric, ForeignKey, func, DateTime


class Promotion:
    __tablename__ = "promotions"
    promotion_id = Column(Integer, primary_key=True)
    pourcentage = Column(Numeric)
    date_debut = Column(DateTime(timezone=False), server_default=func.now())
    dare_fin = Column(DateTime(timezone=False), server_default=func.now())
    product_id = Column(Integer, ForeignKey('products.product_id'))
