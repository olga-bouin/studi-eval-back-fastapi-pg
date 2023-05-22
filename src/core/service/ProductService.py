from sqlalchemy import text
from sqlalchemy.orm import Session

from src.core.service.PromotionService import get_active_promotions


def get_all_products(db: Session):
    stmt = text("SELECT * FROM products")
    results = db.execute(stmt).all()
    return results


def create_product(product, db: Session):
    stmt = text(
        "INSERT INTO products (product_id, libelle, description, prix, promotion, image, catalog_id) VALUES (:product_id, :libelle, :description, :prix, :promotion, :image, :catalog_id)")
    db.execute(stmt, product)
    db.commit()
    return product


def get_max_id(db: Session):
    stmt = text("SELECT MAX(product_id) FROM products")
    results = db.execute(stmt).mappings().all()
    return results[0].max


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
    pourcentages = list(map(lambda promotion: promotion.pourcentage, active_promotions))
    print(pourcentages)
    if len(pourcentages) == 0:
        max_pourcentage = 0
    elif len(pourcentages) == 1:
        max_pourcentage = pourcentages[0]
    else:
        max_pourcentage = max(pourcentages)
    return update_promotion(max_pourcentage, product_id, db)


def compute_all_promotions(db: Session):
    products = get_all_products(db)
    products_ids = map(lambda product: product.product_id, products)
    products_ids_without_doublons = list(set(products_ids))
    results = []
    for product_id in products_ids_without_doublons:
        results.append([product_id, compute_promotion(product_id, db)])
    return results
