
import pandas as pd

df = pd.read_csv('wild_boars.csv')


mean_values = df.mean(numeric_only=True)


with open('mean_values.txt', 'w') as f:
    for col, val in mean_values.items():
        f.write(f"{col}: {val:.2f}\n")

