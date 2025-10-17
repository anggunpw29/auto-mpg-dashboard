# 🚗 Auto MPG Dashboard (Panel + HvPlot)

Created by **Anggun Pangestu Wulandani**  
Tugas Opsi B / Track 2 - Modul 7 Business Intelligence

---

## 📘 Deskripsi Proyek
Dashboard interaktif ini dibangun menggunakan **Python Panel** dan **HvPlot** untuk menganalisis dataset *Auto MPG*.  
Web ini menjawab beberapa pertanyaan analisis utama terkait efisiensi bahan bakar mobil:

1. Bagaimana distribusi nilai MPG pada seluruh mobil?
2. Apakah ada perbedaan rata-rata MPG berdasarkan jumlah silinder?
3. Bagaimana hubungan antara berat mobil dan efisiensi bahan bakar?
4. Bagaimana tren rata-rata MPG berdasarkan tahun model?

---

## 🧠 Insight Utama
- Mobil dengan **4 silinder** cenderung memiliki nilai MPG lebih tinggi (lebih hemat bahan bakar).  
- Terdapat **korelasi negatif** antara berat mobil dan efisiensi bahan bakar.  
- Nilai MPG meningkat dari tahun ke tahun, menunjukkan peningkatan efisiensi mesin.  
- Mobil asal **Jepang** secara umum lebih hemat bahan bakar dibandingkan mobil asal USA.

---

## ⚙️ Cara Menjalankan Secara Lokal

```bash
git clone https://github.com/<username>/auto-mpg-dashboard.git
cd auto-mpg-dashboard

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

panel serve dashboard_auto_mpg.py --allow-websocket-origin="*" --port=5013 --show
```

Aplikasi akan terbuka di browser: [http://localhost:5013](http://localhost:5013)

---

## 🧾 Lisensi
MIT License © 2025 Anggun Pangestu Wulandani

---

> Dibuat dengan ❤️ menggunakan Panel, HvPlot, dan Python
