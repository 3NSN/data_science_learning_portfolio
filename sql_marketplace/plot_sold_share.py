"""Plot the exported SQL results for the synthetic listings."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import pandas as pd

# Read the CSV next to this script; no database connection is needed.
folder = Path(__file__).resolve().parent
data = pd.read_csv(folder / "sold_share_by_category.csv")

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(data["category"], data["sold_percentage"], color="#387d78", width=0.6)
labels = [
    f"{row.sold_percentage:g}% ({row.sold_listings}/{row.total_listings})"
    for row in data.itertuples()
]
ax.bar_label(bars, labels=labels, padding=5)
ax.set_ylim(0, 100)
ax.yaxis.set_major_formatter(PercentFormatter(xmax=100))
ax.set_ylabel("Sold share of listings")
ax.set_title("Sold Share by Category — Synthetic Data", pad=16)
ax.spines[["top", "right"]].set_visible(False)

# Save the chart in the same folder for use in the README.
fig.tight_layout()
fig.savefig(folder / "sold_share_by_category.png", dpi=160)
plt.close(fig)
