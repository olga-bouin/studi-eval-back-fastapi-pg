from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.models.Promotion import Promotion


def get_all_promotions(db: Session):
    stmt = text("SELECT * FROM promotions")
    results = db.execute(stmt).all()
    return results


def create_promotion(promotion: Promotion, db: Session):
    db.add(promotion)
    return promotion
