from pathlib import Path

import pandas as pd
import psycopg


RAW_DIR = Path("data/raw")

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "sales_db",
    "user": "sales_user",
    "password": "sales_password",
}


def load_csv_data():
    customers = pd.read_csv(RAW_DIR / "customers.csv")
    products = pd.read_csv(RAW_DIR / "products.csv")
    orders = pd.read_csv(RAW_DIR / "orders.csv")
    order_items = pd.read_csv(RAW_DIR / "order_items.csv")

    return customers, products, orders, order_items


def insert_data(
    connection,
    customers,
    products,
    orders,
    order_items,
):
    with connection.cursor() as cursor:

        for row in customers.itertuples(index=False):
            cursor.execute(
                """
                INSERT INTO customers (
                    customer_id,
                    name,
                    city,
                    state
                )
                VALUES (%s, %s, %s, %s)
                """,
                tuple(row),
            )

        for row in products.itertuples(index=False):
            cursor.execute(
                """
                INSERT INTO products (
                    product_id,
                    product_name,
                    category,
                    price
                )
                VALUES (%s, %s, %s, %s)
                """,
                tuple(row),
            )

        for row in orders.itertuples(index=False):
            cursor.execute(
                """
                INSERT INTO orders (
                    order_id,
                    customer_id,
                    order_date,
                    status
                )
                VALUES (%s, %s, %s, %s)
                """,
                tuple(row),
            )

        for row in order_items.itertuples(index=False):
            cursor.execute(
                """
                INSERT INTO order_items (
                    order_item_id,
                    order_id,
                    product_id,
                    quantity,
                    unit_price
                )
                VALUES (%s, %s, %s, %s, %s)
                """,
                tuple(row),
            )


def main():
    customers, products, orders, order_items = load_csv_data()

    with psycopg.connect(**DB_CONFIG) as connection:
        insert_data(
            connection,
            customers,
            products,
            orders,
            order_items,
        )

    print(f"Clientes carregados: {len(customers)}")
    print(f"Produtos carregados: {len(products)}")
    print(f"Pedidos carregados: {len(orders)}")
    print(f"Itens carregados: {len(order_items)}")
    print("Carga concluída com sucesso!")


if __name__ == "__main__":
    main()