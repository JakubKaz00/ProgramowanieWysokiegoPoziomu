import sqlite3
import pandas as pd

conn = sqlite3.connect('sales.db')

# a) Wyświetl tylko sprzedaż produktu „Laptop”
query_a = "SELECT * FROM sales WHERE product = 'Laptop'"
df_a = pd.read_sql_query(query_a, conn)
print("a) Sprzedaż produktu 'Laptop':")
print(df_a)

# b) Wyświetl dane tylko z dni 2025-05-07 i 2025-05-08
query_b = "SELECT * FROM sales WHERE date IN ('2025-05-07', '2025-05-08')"
df_b = pd.read_sql_query(query_b, conn)
print("\nb) Sprzedaż z dni 2025-05-07 i 2025-05-08:")
print(df_b)

# c) Wyświetl tylko transakcje, w których cena jednostkowa przekracza 200 zł
query_c = "SELECT * FROM sales WHERE price > 200"
df_c = pd.read_sql_query(query_c, conn)
print("\nc) Transakcje z ceną jednostkową > 200 zł:")
print(df_c)

# d) Oblicz łączną wartość sprzedaży dla każdego produktu
query_d = """
SELECT product, SUM(quantity * price) AS total_sales
FROM sales
GROUP BY product
"""
df_d = pd.read_sql_query(query_d, conn)
print("\nd) Łączna wartość sprzedaży dla każdego produktu:")
print(df_d)


# e) Znajdź dzień z największą liczbą sprzedanych sztuk
query_e = """
SELECT date, SUM(quantity) AS total_quantity
FROM sales
GROUP BY date
ORDER BY total_quantity DESC
LIMIT 1
"""
df_e = pd.read_sql_query(query_e, conn)
print("\ne) Dzień z największą liczbą sprzedanych sztuk:")
print(df_e)

conn.close()
