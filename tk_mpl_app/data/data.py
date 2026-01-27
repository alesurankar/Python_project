import os
import json
import pandas as pd

class Data:
    # -----------------------------
    # Load metadata from JSON
    # -----------------------------
    meta_path = "data/candles.meta.json"
    if os.path.exists(meta_path):
        with open(meta_path, "r") as f:
            meta = json.load(f)
    else:
        # fallback defaults
        meta = {}

    title = meta.get("title", "Untitled")
    label = meta.get("label", "Y")
    x_label = meta.get("x_label", "X")
    y_label = meta.get("y_label", "Y")
    avg = meta.get("avg", False)
    avg_label = meta.get("avg_label", "Average")

    # -----------------------------
    # Load candlestick data
    # -----------------------------
    candlestick_df = pd.read_csv(
        "data/candles.csv",
        index_col="Date",
        parse_dates=True
    )

    # -----------------------------
    # Derived series (used by other charts)
    # -----------------------------
    x = candlestick_df.index.strftime("%b").tolist()   
    y = candlestick_df["Close"].tolist()        

    avg_val = sum(y) / len(y)