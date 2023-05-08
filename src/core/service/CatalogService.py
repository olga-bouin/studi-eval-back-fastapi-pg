from sqlalchemy import text
from sqlalchemy.orm import Session, session

from src.core.models.Catalog import Catalog

catalogs = [{"catalog_id": 1, "libelle": "Catalog 1"},
            {"catalog_id": 2, "libelle": "Catalog 2"}]


def get_all_catalogs(db: Session):
    stmt = text("SELECT * FROM catalog")
    results = db.execute(stmt).all()
    return results


def create_catalog(catalog: Catalog):
    catalogs.append(catalog)
    return catalog
