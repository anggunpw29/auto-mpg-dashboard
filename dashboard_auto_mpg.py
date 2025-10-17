import panel as pn
import pandas as pd
import hvplot.pandas  # pastikan hvplot aktif

pn.extension('tabulator')

# === 1. Baca dataset ===
df = pd.read_csv("Auto_MPG_Clean_for_app.csv")

# Ganti nama kolom supaya rapi
df = df.rename(columns={"model year": "model_year"})

# Mapping asal mobil
mapping = {1: "USA", 2: "Europe", 3: "Japan"}
df["origin"] = df["origin"].map(mapping).fillna(df["origin"].astype(str))

# === 2. Buat grafik ===
mpg_hist = df.hvplot.hist("mpg", bins=20, title="Distribusi MPG", height=250)
avg_cyl = df.groupby("cylinders")["mpg"].mean().reset_index().hvplot.bar(
    x="cylinders", y="mpg", title="Rata-rata MPG per Cylinders", height=250
)
weight_scatter = df.hvplot.scatter(
    x="weight", y="mpg", by="cylinders", title="Weight vs MPG", height=300
)
trend = df.groupby("model_year")["mpg"].mean().reset_index().hvplot.line(
    x="model_year", y="mpg", title="Tren Rata-rata MPG per Tahun", height=250
)

# === 3. Susun layout Panel ===
dashboard = pn.Column(
    "# Auto MPG Dashboard – Anggun Pangestu Wulandani",
    mpg_hist + avg_cyl + weight_scatter + trend
)

# === 4. Tampilkan ke browser ===
dashboard.servable()
