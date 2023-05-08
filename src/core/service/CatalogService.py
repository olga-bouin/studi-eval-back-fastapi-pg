from sqlalchemy import text
from sqlalchemy.orm import Session, session

from src.core.models.Catalog import Catalog


def get_all_catalogs(db: Session):
    stmt = text("SELECT * FROM catalog")
    results = db.execute(stmt).all()
    return results


def create_catalog(catalog: Catalog):
    return catalog
