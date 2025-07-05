
# Dashboard Analisis Data E-Commerce Brasil

Dashboard ini dibuat menggunakan Streamlit sebagai bagian dari submission proyek analisis data Dicoding.

## Cara Menjalankan

1.  Instal dependensi yang dibutuhkan:
   ```
   pip install -r requirements.txt
   ```

2. Jalankan aplikasi Streamlit:
   ```
   streamlit run dashboard.py
   ```

3. Pastikan struktur folder seperti berikut:

```
project-folder/
├── dashboard.py
├── requirements.txt
├── README.md
├── olist_data/
│   ├── olist_orders_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   ├── olist_products_dataset.csv
│   ├── product_category_name_translation.csv
```

## Catatan
Dashboard menampilkan:
- Tren pesanan berhasil dikirim setiap bulan
- Rata-rata payment value per kategori produk
