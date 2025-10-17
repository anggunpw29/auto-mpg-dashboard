# 🚗 Auto MPG Dashboard (Panel + HvPlot)

Created by **Anggun Pangestu Wulandani**  
Tugas Opsi B / Track 2 - Modul 7 Business Intelligence

---

## 📘 Deskripsi Proyek
Dashboard interaktif ini dibangun menggunakan **Python Panel** dan **HvPlot** untuk menganalisis dataset *Auto MPG*.  
Aplikasi ini menjawab beberapa pertanyaan analisis utama terkait efisiensi bahan bakar mobil:

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

panel serve dashboard_auto_mpg.py --allow-websocket-origin="*" --port=5006 --show
```

Aplikasi akan terbuka di browser: [http://localhost:5006](http://localhost:5006)

---

## ☁️ Cara Deploy ke Render

1. Upload repository ini ke GitHub.
2. Buka [https://render.com](https://render.com) → New → Web Service.
3. Hubungkan repo GitHub ini.
4. Build Command:
   ```bash
   pip install -r requirements.txt
   ```
5. Start Command:
   ```bash
   panel serve dashboard_auto_mpg.py --port $PORT --address 0.0.0.0 --allow-websocket-origin=*
   ```

Render akan menyediakan URL publik untuk dashboard kamu 🎉

---

## 🧾 Lisensi
MIT License © 2025 Anggun Pangestu Wulandani

---

> Dibuat dengan ❤️ menggunakan Panel, HvPlot, dan Python