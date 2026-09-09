import random

import pandas as pd
from faker import Faker


ORDER_STATUSES = [
    "completed",
    "processing",
    "cancelled",
]


def generate_orders(customers, quantity=1000):
    fake = Faker("pt_BR")
    Faker.seed(42)
    random.seed(42)

    orders = []

    for order_id in range(1, quantity + 1):
        customer_id = random.choice(
            customers["customer_id"].tolist()
        )

        order = {
            "order_id": order_id,
            "customer_id": customer_id,
            "order_date": fake.date_between(
                start_date="-1y",
                end_date="today",
            ),
            "status": random.choices(
                ORDER_STATUSES,
                weights=[80, 15, 5],
                k=1,
            )[0],
        }

        orders.append(order)

    df_orders = pd.DataFrame(orders)

    assert df_orders["order_id"].is_unique
    assert df_orders["customer_id"].isin(
        customers["customer_id"]
    ).all()

    assert df_orders["order_date"].notna().all()
    assert df_orders["status"].isin(ORDER_STATUSES).all()

    return df_orders