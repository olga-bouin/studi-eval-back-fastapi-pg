from sqlalchemy.orm import Session

from src.core.models.Catalog import Catalog

catalogs = [{"catalog_id": 1, "libelle": "Catalog 1"},
            {"catalog_id": 2, "libelle": "Catalog 2"}]

# def get_all_catalogs(db: Session):
#     return db.query(Catalog).all()

def get_all_catalogs():
    return {"catalogs": catalogs}


def create_catalog(catalog: Catalog):
    catalogs.append(catalog)
    return catalog
