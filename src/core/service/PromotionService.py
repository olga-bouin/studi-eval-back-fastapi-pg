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
    resultat = db.execute(stmt, {"product_id": product_id}).mappings().all()
    return resultat


def get_extended_promotions_data(db: Session):
    stmt = text("SELECT promotions.product_id, libelle, prix, pourcentage, promotion, date_debut, date_fin FROM promotions INNER JOIN products ON promotions.product_id = products.product_id ORDER BY promotions.product_id, promotions.date_debut")
    resultat = db.execute(stmt).mappings().all()
    return resultat