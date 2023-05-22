import uuid

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_all_catalogs():
    response = client.get("/api/catalog/")
    assert response.status_code == 200
    assert response.json() == [{'catalog_id': 8936265, 'libelle': 'Salle de bain'},
                               {'catalog_id': 8936266, 'libelle': 'Cuisine'},
                               {'catalog_id': 8936267, 'libelle': 'Terrasse '},
                               {'catalog_id': 8936268, 'libelle': 'Jardin'},
                               {'catalog_id': 8936269, 'libelle': 'Outillage'},
                               {'catalog_id': 8936270, 'libelle': 'Décoration'},
                               {'catalog_id': 8936271, 'libelle': 'Meubles'},
                               {'catalog_id': 8936272, 'libelle': 'Matérieux'},
                               {'catalog_id': 8936273, 'libelle': 'Électricité'}]


def test_get_catalog():
    response = client.get("/api/catalog/8936265")
    assert response.status_code == 200
    assert response.json() == {'catalog_id': 8936265, 'libelle': 'Salle de bain'}


def test_create_catalog():
    response = client.post("/api/catalog/", json={"catalog_id": 8936274, "libelle": "Test"})
    assert response.status_code == 200
    assert response.json() == {'catalog_id': 8936274, 'libelle': 'Test'}


def test_delete_catalog():
    response = client.delete("/api/catalog/8936274")
    assert response.status_code == 200
    assert response.json() == 8936274


def test_get_all_products():
    response = client.get("/api/products/")
    assert response.status_code == 200
    assert len(response.json()) == 35


def test_get_price():
    response = client.get("/api/products/price/3")
    assert response.status_code == 200
    assert type(response.json()) == float


def test_update_promotion():
    response = client.patch("/api/products/promotion/3", json={"promotion": 1})
    assert response.status_code == 200
    assert response.json() == 163.18


def test_compute_promotion():
    response = client.patch("/api/products/compute_promotions/3")
    assert response.status_code == 200
    assert type(response.json()) == float


def test_compute_all_promotions():
    response = client.patch("/api/products/compute_promotions/")
    assert response.status_code == 200
    assert len(response.json()) == 35


def test_get_all_promotions():
    response = client.get("/api/promotions/")
    assert response.status_code == 200
    assert len(response.json()) > 10


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


def test_create_promotion():
    response = client.post("/api/promotions/", json={"pourcentage": 1, "date_debut": "1900-01-01 00:00:00.000",
                                                     "date_fin": "2023-05-15 06:29:49.000", "product_id": 32})

    assert response.status_code == 200
    assert response.json()["pourcentage"] == 1
    assert response.json()["date_debut"] == "1900-01-01T00:00:00"
    assert response.json()["date_fin"] == "2023-05-15T06:29:49"
    assert response.json()["product_id"] == 32
    assert is_valid_uuid(response.json()["promotion_id"]) == True


def test_get_active_promotions():
    response = client.get("/api/promotions/active_promotions/10")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_extended_promotions_data():
    response = client.get("/api/promotions/extended_promotions_data/")
    assert response.status_code == 200
    assert len(response.json()) > 10
    assert len(response.json()[0]) == 7


def test_compute_promotions():
    response = client.patch("/api/products/compute_promotions/32")
    assert response.status_code == 200
    assert type(response.json()) == float
