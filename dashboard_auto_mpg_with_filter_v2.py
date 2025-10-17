import panel as pn
import pandas as pd
import hvplot.pandas

pn.extension('tabulator')

# === 1. Baca dataset ===
df = pd.read_csv("Auto_MPG_Clean_for_app.csv")
df = df.rename(columns={"model year": "model_year"})

# Mapping asal mobil
mapping = {1: "USA", 2: "Europe", 3: "Japan"}
df["origin"] = df["origin"].map(mapping).fillna(df["origin"].astype(str))

# === 2. Widget Filter ===
origin_filter = pn.widgets.Select(
    name="Pilih Asal Mobil",
    options=["All", "USA", "Europe", "Japan"],
    value="All"
)

cylinder_filter = pn.widgets.IntSlider(
    name="Jumlah Silinder",
    start=3,
    end=8,
    value=4,
    step=1
)

year_filter = pn.widgets.IntRangeSlider(
    name="Tahun Model",
    start=int(df["model_year"].min()),
    end=int(df["model_year"].max()),
    value=(int(df["model_year"].min()), int(df["model_year"].max()))
)

# === 3. Fungsi untuk memperbarui dashboard ===
@pn.depends(origin_filter, cylinder_filter, year_filter)
def update_dashboard(origin, cylinders, year_range):
    subset = df.copy()

    # Terapkan filter
    if origin != "All":
        subset = subset[subset["origin"] == origin]
    if cylinders:
        subset = subset[subset["cylinders"] == cylinders]
    subset = subset[(subset["model_year"] >= year_range[0]) & (subset["model_year"] <= year_range[1])]

    # === Visualisasi ===
    hist = subset.hvplot.hist("mpg", bins=20, title="Distribusi MPG", height=250)
    avg_cyl = subset.groupby("cylinders")["mpg"].mean().reset_index().hvplot.bar(
        x="cylinders", y="mpg", title="Rata-rata MPG per Cylinders", height=250
    )
    scatter = subset.hvplot.scatter(
        x="weight", y="mpg", by="cylinders", title="Weight vs MPG", height=300
    )
    trend = subset.groupby("model_year")["mpg"].mean().reset_index().hvplot.line(
        x="model_year", y="mpg", title="Tren Rata-rata MPG per Tahun", height=250
    )

    return (hist + avg_cyl + scatter + trend).cols(2)

# === 4. Layout utama dashboard ===
dashboard = pn.Column(
    pn.pane.Markdown("## 🚗 Auto MPG Dashboard – Anggun Pangestu Wulandani"),
    pn.Row(origin_filter, cylinder_filter, year_filter),
    update_dashboard
)

dashboard.servable()
