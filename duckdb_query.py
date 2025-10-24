import duckdb

con = duckdb.connect("mini_dw.duckdb")
con.execute("CREATE SCHEMA IF NOT EXISTS dw")

con.execute(
    """
    CREATE TABLE IF NOT EXISTS dw.dim_product AS
    SELECT * FROM read_csv_auto('data/dim/dim_product.csv')
"""
)

con.execute(
    """
    CREATE TABLE IF NOT EXISTS dw.fact_sales AS
    SELECT * FROM read_csv_auto('data/fact/fact_sales.csv')
"""
)

result = con.sql(
    """
    SELECT strftime(order_date, '%Y-%m') AS ym,
           SUM(amount) AS total_sales
    FROM dw.fact_sales
    GROUP BY ym
    ORDER BY ym
"""
).df()

result.to_csv("data/output/monthly_sales.csv", index=False)
print(result)
