import pandas as pd

df = pd.read_csv('wild_boars.csv')


result = []

for gender in df['gender'].unique():
    subset = df[df['gender'] == gender]['length_cm']
    q1 = subset.quantile(0.25)
    q3 = subset.quantile(0.75)
    iqr = q3 - q1
    result.append(f"{gender}: {iqr:.2f} cm")


with open('iqr_by_gender.txt', 'w') as f:
    for line in result:
        f.write(line + '\n')

