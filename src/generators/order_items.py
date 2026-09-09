import random

import pandas as pd
from faker import Faker


def generate_order_items(orders, products):
    fake = Faker("pt_BR")
    Faker.seed(42)
    random.seed(42)

    order_items = []
    order_item_id = 1

    product_ids = products["product_id"].tolist()

    for _, order in orders.iterrows():

        number_of_items = random.randint(1, 5)

        selected_products = random.sample(
            product_ids,
            number_of_items,
        )

        for product_id in selected_products:

            product = products[
                products["product_id"] == product_id
            ].iloc[0]

            item = {
                "order_item_id": order_item_id,
                "order_id": order["order_id"],
                "product_id": product_id,
                "quantity": random.randint(1, 5),
                "unit_price": product["price"],
            }

            order_items.append(item)
            order_item_id += 1

    df_order_items = pd.DataFrame(order_items)

    assert df_order_items["order_item_id"].is_unique

    assert df_order_items["order_id"].isin(
        orders["order_id"]
    ).all()

    assert df_order_items["product_id"].isin(
        products["product_id"]
    ).all()

    assert (df_order_items["quantity"] > 0).all()
    assert (df_order_items["unit_price"] > 0).all()

    return df_order_items