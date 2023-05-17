from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.service.PromotionService import get_active_promotions


def get_all_products(db: Session):
    stmt = text("SELECT * FROM products")
    results = db.execute(stmt).all()
    return results


def get_product(product_id: int, db: Session):
    stmt = text("SELECT * FROM products WHERE product_id = :product_id LIMIT  1")
    results = db.execute(stmt, {"product_id": product_id}).all()
    return results


def get_price(product_id: int, db: Session):
    stmt = text("SELECT prix FROM products WHERE product_id = :product_id")
    results = db.execute(stmt, {"product_id": product_id}).mappings().all()
    return results[0].prix


def update_promotion(promotion_pourcentage: float, product_id: int, db: Session):
    prix = get_price(product_id, db)
    promotion_prix = prix * (1 - promotion_pourcentage / 100)
    promotion_prix_arrondi = round(promotion_prix, 2)
    stmt = text("UPDATE products SET promotion = :promotion WHERE product_id = :product_id")
    db.execute(stmt, {"promotion": promotion_prix_arrondi, "product_id": product_id})
    db.commit()
    return promotion_prix_arrondi


def compute_promotion(product_id: int, db: Session):
    active_promotions = get_active_promotions(product_id, db)
    pourcentages = map(lambda promotion: promotion.pourcentage, active_promotions)
    max_pourcentage = max(pourcentages)
    return update_promotion(max_pourcentage, product_id, db)
