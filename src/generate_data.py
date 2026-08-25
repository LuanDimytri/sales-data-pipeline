import random

import pandas as pd
from faker import Faker

fake = Faker("pt_BR")

Faker.seed(42)
random.seed(42)

products_catalog = {
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

price_ranges = {
    "Periféricos": (50, 1000),
    "Áudio": (50, 1500),
    "Monitores": (500, 5000),
    "Informática": (100, 8000),
    "Eletrônicos": (100, 5000),
    "Acessórios": (10, 500),
}

customers = []

for customer_id in range(1,501):
    customer = {
        "customer_id": customer_id,
        "name": fake.name(),
        "city": fake.city(),
        "state": fake.estado_sigla(),
    }

    customers.append(customer)

df_customers = pd.DataFrame(customers)

products = []

for product_id in range(1, 101):
    category = fake.random_element(
        elements=list(products_catalog.keys())
    )

    product = {
        "product_id": product_id,
        "product_name": fake.random_element(
            elements=products_catalog[category]
        ),
        "category": category,
        "price": round(
            random.uniform(
                price_ranges[category][0],
                price_ranges[category][1]
            ),
            2
        ),
    }

    products.append(product)

df_products = pd.DataFrame(products)

print(df_customers)
print(df_products)

df_customers.to_csv(
    "data/raw/customers.csv",
    index=False
)
df_products.to_csv(
    "data/raw/products.csv",
    index=False
)