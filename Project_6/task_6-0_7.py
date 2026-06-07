import pandas as pd

df = pd.read_csv('wild_boars.csv')

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

with open('dispersion_std_cv.txt', 'w') as f:
    for col in numeric_cols:
        var_val = df[col].var()
        std_val = df[col].std()
        cv_val = (std_val / df[col].mean()) * 100 if df[col].mean() != 0 else float('nan')
        
        f.write(f"{col}:\n")
        f.write(f"  Variance: {var_val:.2f}\n")
        f.write(f"  Standard deviation: {std_val:.2f}\n")
        f.write(f"  Coefficient of variation: {cv_val:.2f}%\n\n")

