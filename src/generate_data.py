from src.generators.customers import generate_customers
from src.generators.products import generate_products


customers = generate_customers(500)
products = generate_products(100)


customers.to_csv(
    "data/raw/customers.csv",
    index=False,
)

products.to_csv(
    "data/raw/products.csv",
    index=False,
)


print(f"Clientes gerados: {len(customers)}")
print(f"Produtos gerados: {len(products)}")