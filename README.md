# Sales Data Pipeline

Pipeline de dados desenvolvido em Python para geração, transformação, armazenamento e análise de dados de vendas, utilizando PostgreSQL, Docker, SQL e Power BI.

O projeto simula um cenário de vendas com dados sintéticos e implementa um fluxo completo de dados, desde a geração dos registros até a disponibilização de indicadores para análise.

---

## 📌 Visão geral

O projeto foi desenvolvido com o objetivo de aplicar, na prática, conceitos de **Data Engineering e Data Analytics**, construindo um pipeline capaz de:

- Gerar dados sintéticos de vendas;
- Validar os dados gerados;
- Transformar os dados utilizando Python e Pandas;
- Armazenar os dados em PostgreSQL;
- Executar análises utilizando SQL;
- Disponibilizar os dados para o Power BI;
- Criar um dashboard interativo para análise das vendas.

---

## 🏗️ Arquitetura

```text
┌──────────────────────┐
│   Python + Faker     │
│   Geração de dados   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      CSV / Raw       │
│   Dados sintéticos   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Python + Pandas    │
│         ETL          │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     PostgreSQL       │
│  Armazenamento + SQL │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│       Power BI       │
│     Dashboard        │
└──────────────────────┘
```

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Geração e transformação dos dados |
| Pandas | Manipulação e transformação dos dados |
| Faker | Geração de dados sintéticos |
| PostgreSQL | Banco de dados relacional |
| SQL | Consultas e análises |
| Docker | Execução do PostgreSQL |
| Power BI | Visualização e análise |
| Git | Controle de versão |
| GitHub | Versionamento e documentação |

---

## 📂 Estrutura do projeto

```text
sales-data-pipeline/
│
├── data/
│   └── raw/
│       ├── customers.csv
│       ├── products.csv
│       ├── orders.csv
│       └── order_items.csv
│
├── sql/
│   ├── schema.sql
│   └── analysis.sql
│
├── src/
│   ├── __init__.py
│   ├── generate_data.py
│   ├── etl.py
│   ├── load_database.py
│   │
│   └── generators/
│       ├── __init__.py
│       ├── customers.py
│       ├── products.py
│       ├── orders.py
│       └── order_items.py
│
├── tests/
│
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 📊 Modelo de dados

O projeto utiliza quatro entidades principais.

### Customers

Informações dos clientes.

```text
customer_id
name
city
state
```

### Products

Catálogo de produtos.

```text
product_id
product_name
category
price
```

### Orders

Pedidos realizados pelos clientes.

```text
order_id
customer_id
order_date
status
```

### Order Items

Itens pertencentes a cada pedido.

```text
order_item_id
order_id
product_id
quantity
unit_price
```

Essas entidades são relacionadas através de chaves primárias e estrangeiras, permitindo realizar análises de vendas, produtos, clientes e períodos.

---

# 📦 Dados utilizados

Os dados utilizados neste projeto são **sintéticos**, gerados através de Python e Faker.

A base contém:

| Entidade | Registros |
|---|---:|
| Clientes | 500 |
| Produtos | 100 |
| Pedidos | 1.000 |
| Itens de pedidos | 2.996 |

A geração utiliza uma seed fixa para permitir a reprodução dos dados.

---

# 🔄 Pipeline de dados

## 1. Geração dos dados

A geração dos dados é realizada pelos módulos localizados em:

```text
src/generators/
```

Cada módulo é responsável pela geração de uma entidade específica:

- `customers.py`
- `products.py`
- `orders.py`
- `order_items.py`

O arquivo `generate_data.py` coordena todo o processo.

Para gerar os dados:

```powershell
python -m src.generate_data
```

Resultado esperado:

```text
Clientes gerados: 500
Produtos gerados: 100
Pedidos: 1000
Itens de pedidos: 2996
```

---

## 2. ETL

O processo de ETL é realizado pelo arquivo:

```text
src/etl.py
```

Durante essa etapa são realizadas transformações como:

- leitura dos arquivos CSV;
- cálculo do valor total dos itens;
- associação entre pedidos e itens;
- identificação do status dos pedidos;
- cálculo da receita efetiva;
- geração dos dados processados.

O valor total de cada item é calculado através da multiplicação de:

```text
quantidade × preço unitário
```

A receita efetiva considera apenas pedidos com status:

```text
completed
```

Para executar o ETL:

```powershell
python -m src.etl
```

---

## 3. PostgreSQL

O banco de dados PostgreSQL é executado através do Docker.

Para iniciar o banco:

```powershell
docker compose up -d
```

Configuração utilizada no ambiente local:

```text
Database: sales_db
User: sales_user
Password: sales_password
Host: localhost
Port: 5432
```

---

## 4. Criação das tabelas

O schema do banco está localizado em:

```text
sql/schema.sql
```

As principais tabelas são:

```text
customers
products
orders
order_items
```

---

## 5. Carga dos dados

Após iniciar o PostgreSQL, os dados podem ser carregados utilizando:

```powershell
python -m src.load_database
```

Resultado esperado:

```text
Clientes carregados: 500
Produtos carregados: 100
Pedidos carregados: 1000
Itens carregados: 2996
Carga concluída com sucesso!
```

O processo de carga foi implementado para permitir novas execuções sem gerar conflitos de chave primária.

---

# 🔎 Análises SQL

As principais consultas analíticas estão disponíveis em:

```text
sql/analysis.sql
```

Entre as análises realizadas estão:

- receita efetiva;
- quantidade de pedidos por status;
- receita mensal;
- produtos mais vendidos;
- produtos com maior faturamento;
- faturamento por categoria;
- ticket médio;
- clientes com maior volume de compras.

---

# 📈 Principais resultados

Com os dados atualmente gerados, o pipeline apresentou:

| Indicador | Resultado |
|---|---:|
| Receita bruta | R$ 14.375.433,06 |
| Receita efetiva | R$ 11.326.976,72 |
| Pedidos concluídos | 805 |
| Ticket médio | R$ 14.070,78 |

A receita efetiva considera apenas pedidos com status `completed`.

Pedidos com status `processing` e `cancelled` não são contabilizados na receita efetiva.

---

# 📊 Dashboard Power BI

Os dados armazenados no PostgreSQL são utilizados como fonte para um dashboard desenvolvido no Power BI.

O dashboard apresenta:

- Receita efetiva;
- Pedidos concluídos;
- Ticket médio;
- Receita efetiva por mês;
- Receita efetiva por categoria;
- Receita efetiva por produto;
- Filtro por categoria;
- Filtro por estado;
- Filtro por período.

### Indicadores principais

```text
Receita Efetiva     → R$ 11,33 Mi
Pedidos Concluídos  → 805
Ticket Médio        → R$ 14,07 Mil
```

O dashboard permite filtrar os dados por categoria, estado e período, possibilitando diferentes perspectivas sobre o desempenho das vendas.

> O dashboard foi desenvolvido no Power BI utilizando o PostgreSQL como fonte de dados.

---

# 🚀 Como executar o projeto

## Pré-requisitos

Para executar o projeto, é necessário ter instalado:

- Python 3.10 ou superior;
- Docker;
- Git.

---

## 1. Clonar o repositório

```powershell
git clone https://github.com/LuanDimytri/sales-data-pipeline.git
```

Entrar na pasta:

```powershell
cd sales-data-pipeline
```

---

## 2. Criar o ambiente virtual

No Windows:

```powershell
python -m venv .venv
```

Ativar o ambiente:

```powershell
.venv\Scripts\Activate.ps1
```

---

## 3. Instalar as dependências

```powershell
pip install -r requirements.txt
```

---

## 4. Iniciar o PostgreSQL

```powershell
docker compose up -d
```

Verificar o container:

```powershell
docker compose ps
```

---

## 5. Gerar os dados

```powershell
python -m src.generate_data
```

---

## 6. Executar o ETL

```powershell
python -m src.etl
```

---

## 7. Criar as tabelas do banco

Executar o arquivo:

```text
sql/schema.sql
```

no PostgreSQL.

---

## 8. Carregar os dados

```powershell
python -m src.load_database
```

---

## 9. Executar as análises

As consultas analíticas estão disponíveis em:

```text
sql/analysis.sql
```

---

## 10. Conectar ao Power BI

Utilizar os seguintes dados para conexão:

```text
Servidor: localhost
Porta: 5432
Banco: sales_db
```

Após a conexão, os dados do PostgreSQL podem ser utilizados para construção ou atualização do dashboard.

---

# ♻️ Reprodutibilidade

O projeto utiliza seeds fixas durante a geração dos dados, permitindo reproduzir o mesmo conjunto de dados em diferentes execuções.

O processo também possui validações para garantir a integridade dos registros gerados.

A carga no PostgreSQL pode ser executada novamente sem gerar duplicidade dos registros.

Isso facilita testes, desenvolvimento e reprodução do pipeline.

---

# 🔮 Próximas melhorias

Possíveis evoluções para o projeto:

- [ ] Implementação de testes automatizados;
- [ ] Implementação de logging;
- [ ] Tratamento de exceções mais robusto;
- [ ] Utilização de variáveis de ambiente para credenciais;
- [ ] Containerização completa da aplicação;
- [ ] Automação da execução do pipeline;
- [ ] Implementação de orquestração;
- [ ] Expansão das análises no Power BI.

---

# 👨‍💻 Autor

**Luan Dimytri**

Estudante de Ciência da Computação com interesse em desenvolvimento, dados e automação.

Este projeto faz parte do meu portfólio e foi desenvolvido para aplicar, na prática, conhecimentos relacionados a:

- Python;
- ETL;
- SQL;
- PostgreSQL;
- Docker;
- Power BI;
- Git;
- GitHub.

---

## 📄 Licença

Projeto desenvolvido para fins educacionais e de portfólio.