import pandas as pd

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Calculate the difference between consecutive values of 'deviation_normal'
df['deviation_diff'] = df['deviation_normal'].diff()

# Identify the inflection/shift points
df['feature_shift'] = df['deviation_diff'].apply(lambda x: 1 if x != 0 else 0)

# Save the updated dataset
df.to_csv('your_dataset_with_feature_shift.csv', index=False)
