from pathlib import Path

import pandas as pd


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def load_data():
    customers = pd.read_csv(RAW_DIR / "customers.csv")
    products = pd.read_csv(RAW_DIR / "products.csv")
    orders = pd.read_csv(RAW_DIR / "orders.csv")
    order_items = pd.read_csv(RAW_DIR / "order_items.csv")

    return customers, products, orders, order_items


def transform_order_items(order_items):
    order_items = order_items.copy()

    order_items["total_price"] = (
        order_items["quantity"] * order_items["unit_price"]
    )

    return order_items


def transform_sales(order_items, orders):
    sales = order_items.merge(
        orders[
            [
                "order_id",
                "order_date",
                "status",
            ]
        ],
        on="order_id",
        how="left",
    )

    assert sales["order_date"].notna().all()
    assert sales["status"].notna().all()

    return sales


def calculate_effective_revenue(sales):
    sales = sales.copy()

    sales["effective_revenue"] = sales["total_price"].where(
        sales["status"] == "completed",
        0,
    )

    return sales


def save_processed_data(sales):
    PROCESSED_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path = PROCESSED_DIR / "sales.csv"

    sales.to_csv(
        output_path,
        index=False,
    )

    return output_path


if __name__ == "__main__":
    customers, products, orders, order_items = load_data()

    order_items = transform_order_items(order_items)

    sales = transform_sales(
        order_items,
        orders,
    )

    sales = calculate_effective_revenue(sales)

    output_path = save_processed_data(sales)

    print(f"Clientes carregados: {len(customers)}")
    print(f"Produtos carregados: {len(products)}")
    print(f"Pedidos carregados: {len(orders)}")
    print(f"Itens carregados: {len(order_items)}")

    print("\nExemplo das vendas transformadas:")
    print(
        sales[
            [
                "order_item_id",
                "order_id",
                "product_id",
                "quantity",
                "unit_price",
                "total_price",
                "effective_revenue",
                "order_date",
                "status",
            ]
        ].head()
    )

    print("\nResumo financeiro:")
    print(f"Faturamento bruto: R$ {sales['total_price'].sum():,.2f}")
    print(
        f"Faturamento efetivo: "
        f"R$ {sales['effective_revenue'].sum():,.2f}"
    )

    print(f"\nArquivo processado salvo em: {output_path}")