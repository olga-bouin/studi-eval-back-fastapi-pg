from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.models.Promotion import Promotion


def get_all_promotions(db: Session):
    stmt = text("SELECT * FROM promotions")
    results = db.execute(stmt).all()
    return results


def create_promotion(promotion: Promotion, db: Session):
    stmt = text("INSERT INTO promotions (promotion_id, pourcentage, date_debut, date_fin, product_id) VALUES (:promotion_id, :pourcentage, :date_debut, :date_fin, :product_id)")
    db.execute(stmt, promotion.dict())
    db.commit()
    return promotion
