import pandas as pd
import matplotlib.pyplot as plt

file_path = "Section2/Crash_Data.csv"
df = pd.read_csv(file_path)

df_2021 = df[df['Year'] == 2021]

average_age_by_gender = df_2021.groupby('Gender')['Age'].mean().reset_index()

print("Average age of individuals who died in traffic accidents in Australia in 2021 by gender:")
print(average_age_by_gender)

csv_path = "results.csv"
average_age_by_gender.to_csv(csv_path, index=False)

print(f"The results have been saved to: {csv_path}")


