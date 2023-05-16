from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.models.Promotion import Promotion


def get_all_promotions(db: Session):
    stmt = text("SELECT * FROM promotions")
    results = db.execute(stmt).all()
    return results


def create_promotion(promotion: Promotion, db: Session):
    stmt = text(
        "INSERT INTO promotions (promotion_id, pourcentage, date_debut, date_fin, product_id) VALUES (:promotion_id, :pourcentage, :date_debut, :date_fin, :product_id)")
    db.execute(stmt, promotion)
    db.commit()
    return promotion


def get_active_promotions(product_id: int, db: Session):
    stmt = text("SELECT promotion_id, pourcentage, product_id FROM promotions WHERE product_id = :product_id AND date_debut <= NOW() AND date_fin >= NOW()")
    resultat = db.execute(stmt, {"product_id": product_id}).mappings().all();
    return resultat
