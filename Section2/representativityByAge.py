import pandas as pd

file_path = "Section2/Crash_Data.csv"
df = pd.read_csv(file_path)

grouped_data = df.groupby(['Age Group', 'Crash Type']).size().reset_index(name='Count')

grouped_data['Representativity'] = grouped_data.groupby('Crash Type')['Count'].transform(lambda x: (x / x.sum()) * 100)

print("Table of Representativity of Age Groups in Relation to Crash Type:")
print(grouped_data)

csv_path = "representativity_results.csv"
grouped_data.to_csv(csv_path, index=False)

print(f"The results have been saved to: {csv_path}")
