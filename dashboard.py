
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Dashboard E-Commerce", layout="wide")
st.title("📦 Dashboard Analisis Data E-Commerce Brasil")

# Load data
orders = pd.read_csv("olist_data/olist_orders_dataset.csv", parse_dates=["order_purchase_timestamp"])
order_items = pd.read_csv("olist_data/olist_order_items_dataset.csv")
payments = pd.read_csv("olist_data/olist_order_payments_dataset.csv")
products = pd.read_csv("olist_data/olist_products_dataset.csv")
categories = pd.read_csv("olist_data/product_category_name_translation.csv")

# Preprocessing
orders = orders[orders["order_status"] == "delivered"].copy()
orders["month_year"] = orders["order_purchase_timestamp"].dt.to_period("M").astype(str)

# Jumlah pesanan per bulan
monthly = (
    orders.groupby("month_year").size().reset_index(name="total_orders")
)

# Tambahkan fitur interaktif: filter bulan
st.sidebar.header("🔎 Filter Data")
selected_months = st.sidebar.multiselect(
    "Pilih Bulan (opsional):",
    options=monthly["month_year"].unique(),
    default=monthly["month_year"].unique()
)
filtered_monthly = monthly[monthly["month_year"].isin(selected_months)]

# Rata-rata payment per kategori
merged = order_items.merge(payments, on="order_id")
merged = merged.merge(products, on="product_id")
merged = merged.merge(categories, on="product_category_name", how="left")
avg_payment = (
    merged.groupby("product_category_name_english")["payment_value"]
    .mean().sort_values(ascending=False).head(10).reset_index()
)

# Layout dua kolom
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Jumlah Pesanan yang Dikirim per Bulan (Filtered)")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=filtered_monthly, x="month_year", y="total_orders", marker="o", ax=ax1)
    ax1.set_xticklabels(filtered_monthly["month_year"], rotation=45)
    ax1.set_xlabel("Bulan")
    ax1.set_ylabel("Jumlah Pesanan")
    ax1.grid(True)
    st.pyplot(fig1)

with col2:
    st.subheader("💳 Rata-rata Payment per Kategori Produk (Top 10)")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.barplot(data=avg_payment, x="payment_value", y="product_category_name_english", palette="Blues_d", ax=ax2)
    ax2.set_xlabel("Rata-rata Payment")
    ax2.set_ylabel("Kategori Produk")
    st.pyplot(fig2)

# Footer
st.markdown("---")
st.markdown("🧾 **Catatan:** Dashboard ini menampilkan ringkasan hasil analisis berdasarkan data transaksi e-commerce Brasil dari Olist. "
            "Gunakan fitur sidebar untuk memfilter data bulanan sesuai kebutuhan.")
