from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.models.Catalog import Catalog


def get_all_catalogs(db: Session):
    stmt = text("SELECT * FROM catalog")
    results = db.execute(stmt).all()
    return results


def create_catalog(catalog: Catalog, db: Session):
    stmt = text("INSERT INTO catalog (catalog_id, libelle) VALUES (:catalog_id, :libelle)")
    db.execute(stmt, {"catalog_id": catalog.catalog_id, "libelle": catalog.libelle})
    db.commit()
    return catalog


def delete_catalog(catalog_id: int, db: Session):
    stmt = text("DELETE FROM catalog WHERE catalog_id = :catalog_id")
    db.execute(stmt, {"catalog_id": catalog_id})
    db.commit()
    return catalog_id
