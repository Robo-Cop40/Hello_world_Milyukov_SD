import pandas as pd
df = pd.read_csv('wild_boars.csv')
print("Tusk length (cm):")
print(df['tusk_length_cm'])
min_tusk = df['tusk_length_cm'].min()
max_tusk = df['tusk_length_cm'].max()
print(f"\nShortest tusk length: {min_tusk:.2f} cm")
print(f"Longest tusk length: {max_tusk:.2f} cm")