import random

import pandas as pd
from faker import Faker


PRODUCTS_CATALOG = {
    "Periféricos": [
        "Mouse Gamer",
        "Teclado Mecânico",
        "Mousepad Gamer",
        "Controle USB",
    ],
    "Áudio": [
        "Headset Gamer",
        "Fone Bluetooth",
        "Caixa de Som",
        "Microfone USB",
    ],
    "Monitores": [
        "Monitor 24",
        "Monitor 27",
        "Monitor Ultrawide",
    ],
    "Informática": [
        "SSD 1TB",
        "Memória RAM 16GB",
        "Placa de Vídeo",
        "Processador",
    ],
    "Eletrônicos": [
        "Webcam Full HD",
        "Smartwatch",
        "Tablet",
        "Hub USB",
    ],
    "Acessórios": [
        "Cabo HDMI",
        "Cabo USB-C",
        "Suporte para Notebook",
        "Adaptador USB",
    ],
}

PRICE_RANGES = {
    "Periféricos": (50, 1000),
    "Áudio": (50, 1500),
    "Monitores": (500, 5000),
    "Informática": (100, 8000),
    "Eletrônicos": (100, 5000),
    "Acessórios": (10, 500),
}


def generate_products(quantity=100):
    fake = Faker("pt_BR")
    Faker.seed(42)
    random.seed(42)

    products = []

    for product_id in range(1, quantity + 1):
        category = fake.random_element(
            elements=list(PRODUCTS_CATALOG.keys())
        )

        product = {
            "product_id": product_id,
            "product_name": fake.random_element(
                elements=PRODUCTS_CATALOG[category]
            ),
            "category": category,
            "price": round(
                random.uniform(
                    PRICE_RANGES[category][0],
                    PRICE_RANGES[category][1]
                ),
                2,
            ),
        }

        products.append(product)

    df_products = pd.DataFrame(products)

    assert df_products["product_id"].is_unique
    assert df_products["product_name"].notna().all()
    assert df_products["category"].notna().all()
    assert df_products["price"].notna().all()
    assert (df_products["price"] > 0).all()

    return df_products