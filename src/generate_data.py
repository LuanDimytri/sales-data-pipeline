import pandas as pd
from faker import Faker

fake = Faker("pt_BR")

customers = []

for customer_id in range(1, 11):
    customer = {
        "customer_id": customer_id,
        "name": fake.name(),
        "city": fake.city(),
        "state": fake.estado_sigla(),
    }

    customers.append(customer)

df_customers = pd.DataFrame(customers)

print(df_customers)

df_customers.to_csv(
    "data/raw/customers.csv",
    index=False
)