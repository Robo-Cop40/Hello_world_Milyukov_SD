import pandas as pd

df = pd.read_csv('wild_boars.csv')

percentiles = [0.25, 0.50, 0.75, 0.90, 0.95, 1.00]
percentile_names = {
    0.25: "Percentile 25 (Q1)",
    0.50: "Median 50 (Q2)",
    0.75: "Percentile 75 (Q3)",
    0.90: "Percentile 90",
    0.95: "Percentile 95",
    1.00: "Max"
}

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

with open('percentiles_all_columns.txt', 'w') as f:
    for col in numeric_cols:
        f.write(f"\n{col}:\n")
        for p in percentiles:
            val = df[col].quantile(p)
            f.write(f"{percentile_names[p]}:\t{val:.1f}\n")

