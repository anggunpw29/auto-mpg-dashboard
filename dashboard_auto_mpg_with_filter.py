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

# === 2. Buat widget filter ===
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

# === 3. Fungsi untuk update grafik berdasarkan filter ===
@pn.depends(origin_filter, cylinder_filter)
def update_dashboard(origin, cylinders):
    subset = df.copy()
    if origin != "All":
        subset = subset[subset["origin"] == origin]
    if cylinders:
        subset = subset[subset["cylinders"] == cylinders]

    # Histogram MPG
    hist = subset.hvplot.hist("mpg", bins=20, title="Distribusi MPG", height=250)

    # Bar chart rata-rata MPG per Cylinders
    avg_cyl = subset.groupby("cylinders")["mpg"].mean().reset_index().hvplot.bar(
        x="cylinders", y="mpg", title="Rata-rata MPG per Cylinders", height=250
    )

    # Scatter plot Weight vs MPG
    scatter = subset.hvplot.scatter(
        x="weight", y="mpg", by="cylinders", title="Weight vs MPG", height=300
    )

    # Line chart tren MPG per tahun
    trend = subset.groupby("model_year")["mpg"].mean().reset_index().hvplot.line(
        x="model_year", y="mpg", title="Tren Rata-rata MPG per Tahun", height=250
    )

    return (hist + avg_cyl + scatter + trend).cols(2)

# === 4. Layout dashboard ===
dashboard = pn.Column(
    pn.pane.Markdown("## 🚗 Auto MPG Dashboard – Anggun Pangestu Wulandani"),
    pn.Row(origin_filter, cylinder_filter),
    update_dashboard
)

dashboard.servable()
