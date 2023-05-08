from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.models.Product import Product


def get_all_products(db: Session):
    stmt = text("SELECT * FROM products")
    results = db.execute(stmt).all()
    return results


def create_product(product: Product):
    return product
