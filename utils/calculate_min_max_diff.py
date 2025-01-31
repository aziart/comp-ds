import pandas as pd

# Load your dataset
df = pd.read_csv('your_dataset.csv')

# Calculate the difference between the maximum and minimum values of 'deviation_normal' for each 'machine_id'
df['feature_min_max_diff'] = df.groupby('machine_id')['deviation_normal'].transform(lambda x: x.max() - x.min())

# Save the updated dataset
df.to_csv('your_dataset_with_feature_min_max_diff.csv', index=False)
