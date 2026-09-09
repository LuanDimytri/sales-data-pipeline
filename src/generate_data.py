from src.generators.customers import generate_customers
from src.generators.products import generate_products
from src.generators.orders import generate_orders
from src.generators.order_items import generate_order_items


customers = generate_customers(500)

products = generate_products(100)

orders = generate_orders(
    customers,
    quantity=1000,
)

order_items = generate_order_items(
    orders,
    products,
)


customers.to_csv(
    "data/raw/customers.csv",
    index=False,
)

products.to_csv(
    "data/raw/products.csv",
    index=False,
)

orders.to_csv(
    "data/raw/orders.csv",
    index=False,
)

order_items.to_csv(
    "data/raw/order_items.csv",
    index=False,
)


print(f"Clientes gerados: {len(customers)}")
print(f"Produtos gerados: {len(products)}")
print(f"Pedidos gerados: {len(orders)}")
print(f"Itens de pedidos gerados: {len(order_items)}")