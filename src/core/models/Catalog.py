from sqlalchemy import Integer, Column, PrimaryKeyConstraint, String

from src.core.database.database import connect_with_connector


class Catalog(connect_with_connector()):
    __tablename__ = "Catalog"
    catalog_id = Column(Integer, index=True, nullable=False, autoincrement=True)
    libelle = Column(String(144), nullable=False)

    __table_args__ = (PrimaryKeyConstraint('catalog_id'), {},)