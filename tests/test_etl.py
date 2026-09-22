import pandas as pd

from src.etl import (
    calculate_effective_revenue,
    transform_order_items,
    transform_sales,
)


def test_transform_order_items():
    order_items = pd.DataFrame(
        {
            "order_item_id": [1, 2],
            "order_id": [1, 1],
            "product_id": [10, 20],
            "quantity": [2, 3],
            "unit_price": [100.0, 50.0],
        }
    )

    result = transform_order_items(order_items)

    assert "total_price" in result.columns
    assert result["total_price"].tolist() == [200.0, 150.0]


def test_transform_sales():
    order_items = pd.DataFrame(
        {
            "order_item_id": [1],
            "order_id": [1],
            "product_id": [10],
            "quantity": [2],
            "unit_price": [100.0],
            "total_price": [200.0],
        }
    )

    orders = pd.DataFrame(
        {
            "order_id": [1],
            "order_date": ["2026-01-01"],
            "status": ["completed"],
        }
    )

    products = pd.DataFrame(
        {
            "product_id": [10],
            "product_name": ["Mouse Gamer"],
            "category": ["Periféricos"],
        }
    )

    result = transform_sales(
        order_items,
        orders,
        products,
    )

    assert len(result) == 1
    assert result.loc[0, "product_name"] == "Mouse Gamer"
    assert result.loc[0, "category"] == "Periféricos"


def test_effective_revenue():
    sales = pd.DataFrame(
        {
            "total_price": [
                100.0,
                200.0,
                300.0,
            ],
            "status": [
                "completed",
                "cancelled",
                "processing",
            ],
        }
    )

    result = calculate_effective_revenue(sales)

    assert result["effective_revenue"].tolist() == [
        100.0,
        0.0,
        0.0,
    ]