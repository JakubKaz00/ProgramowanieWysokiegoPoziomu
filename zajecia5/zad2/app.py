import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1)
def load_data():
    conn = sqlite3.connect('sales.db')
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    return df

def insert_record(product, quantity, price, date):
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sales (product, quantity, price, date) VALUES (?, ?, ?, ?)",
        (product, quantity, price, date)
    )
    conn.commit()
    conn.close()


st.title("📊 Aplikacja Sprzedażowa")

# 2) Dodawanie rekordu
st.header("➕ Dodaj nową sprzedaż")
with st.form("add_sale_form"):
    col1, col2 = st.columns(2)
    product = col1.text_input("Produkt")
    quantity = col1.number_input("Ilość", min_value=1, step=1)
    price = col2.number_input("Cena jednostkowa", min_value=0.0, step=0.01)
    date = col2.date_input("Data")
    submitted = st.form_submit_button("Dodaj rekord")

    if submitted:
        insert_record(product, quantity, price, date.strftime("%Y-%m-%d"))
        st.success("✅ Rekord dodany!")
        st.balloons()

# 3) Wyświetlanie i filtrowanie danych
st.header("📋 Tabela sprzedaży")

df = load_data()

product_filter = st.selectbox("Filtruj po produkcie", options=["Wszystkie"] + sorted(df['product'].unique().tolist()))

if product_filter != "Wszystkie":
    df = df[df['product'] == product_filter]

st.dataframe(df)

# 4) Wykresy
st.header("📈 Statystyki sprzedaży")

# a)
st.subheader("Sprzedaż dzienna (wartość)")
df['total_value'] = df['quantity'] * df['price']
daily_sales = df.groupby('date')['total_value'].sum().reset_index()

fig1, ax1 = plt.subplots()
ax1.plot(daily_sales['date'], daily_sales['total_value'], marker='o')
ax1.set_xlabel("Data")
ax1.set_ylabel("Wartość sprzedaży")
ax1.set_title("Sprzedaż dzienna")
st.pyplot(fig1)

# b)
st.subheader("Suma sprzedanych sztuk wg produktu")
product_sales = df.groupby('product')['quantity'].sum().reset_index()

fig2, ax2 = plt.subplots()
ax2.bar(product_sales['product'], product_sales['quantity'], color='skyblue')
ax2.set_xlabel("Produkt")
ax2.set_ylabel("Suma ilości")
ax2.set_title("Sprzedaż wg typu produktu")
st.pyplot(fig2)
