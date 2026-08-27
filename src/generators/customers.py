import pandas as pd
from faker import Faker


def generate_customers(quantity=500):
    fake = Faker("pt_BR")
    Faker.seed(42)

    customers = []

    for customer_id in range(1, quantity + 1):
        customer = {
            "customer_id": customer_id,
            "name": fake.name(),
            "city": fake.city(),
            "state": fake.estado_sigla(),
        }

        customers.append(customer)

    df_customers = pd.DataFrame(customers)

    assert df_customers["customer_id"].is_unique
    assert df_customers["name"].notna().all()
    assert df_customers["city"].notna().all()
    assert df_customers["state"].notna().all()

    return df_customers